# -*- coding: utf-8 -*-
# Copyright © 2025 Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""
Spyder AsyncDispatcher API.

This module provides an class decorator `AsyncDispatcher` to run coroutines on
dedicated async loops, including utilities for patching loops, managing
concurrency tasks, and executing callbacks safely within Qt applications.
"""

from __future__ import annotations

import asyncio
import asyncio.events
import atexit
import contextlib
import functools
import logging
import os
import sys
import threading
import typing
from asyncio.futures import (
    _chain_future,  # type: ignore[attr-defined] # noqa: PLC2701
)
from asyncio.tasks import (
    _current_tasks,  # type: ignore[attr-defined] # noqa: PLC2701
)
from concurrent.futures import CancelledError, Future
from heapq import heappop

if sys.version_info >= (3, 10):
    from typing import ParamSpec  # noqa: ICN003
else:
    from typing_extensions import ParamSpec

from qtpy.QtCore import QCoreApplication, QEvent, QObject

_logger = logging.getLogger(__name__)

LoopID = typing.Union[typing.Hashable, asyncio.AbstractEventLoop]

_P = ParamSpec("_P")
_T = typing.TypeVar("_T")
_RT = typing.TypeVar("_RT")


class AsyncDispatcher(typing.Generic[_RT]):
    """Decorator to run a coroutine in a specific event loop."""

    __rlock = threading.RLock()

    __closed = False
    __running_threads: typing.ClassVar[dict[typing.Hashable, _LoopRunner]] = {}
    _running_tasks: typing.ClassVar[list[Future]] = []

    @typing.overload
    def __init__(
        self: AsyncDispatcher[DispatcherFuture[_T]],
        *,
        loop: LoopID | None = ...,
        early_return: typing.Literal[True] = ...,
        return_awaitable: typing.Literal[False] = ...,
    ): ...

    @typing.overload
    def __init__(
        self: AsyncDispatcher[typing.Awaitable[_T]],
        *,
        loop: LoopID | None = ...,
        early_return: typing.Literal[True] = ...,
        return_awaitable: typing.Literal[True] = ...,
    ): ...

    @typing.overload
    def __init__(
        self: AsyncDispatcher[_T],
        *,
        loop: LoopID | None = ...,
        early_return: typing.Literal[False] = ...,
        return_awaitable: typing.Literal[False] = ...,
    ): ...

    @typing.overload
    def __init__(
        self: AsyncDispatcher[typing.Awaitable[_T]],
        *,
        loop: LoopID | None = ...,
        early_return: typing.Literal[False] = ...,
        return_awaitable: typing.Literal[True] = ...,
    ): ...

    def __init__(
        self,
        *,
        loop: LoopID | None = None,
        early_return: bool = True,
        return_awaitable: bool = False,
    ):
        """
        Decorate a coroutine to run in a specific event loop.

        The `loop` parameter can be an existing loop or a hashable to identify
        an existing/new one (to be) created by the AsyncDispatcher. If the
        loop is not running, it will be started in a new thread and managed by
        the AsyncDispatcher.

        This instance can be called with the same arguments as the coroutine it
        wraps and will return a concurrent Future object, or an awaitable
        Future for the current running event loop or the result of the
        coroutine depending on the `early_return` and `return_awaitable`
        parameters.

        Usage
        -----
        Non-Blocking usage (returns a concurrent Future):
        ```
        @AsyncDispatcher()
        async def my_coroutine(...):
            ...

        future = my_coroutine(...)  # Non-blocking call

        result = future.result()  # Blocking call
        ```

        Blocking usage (returns the result):
        ```
        @AsyncDispatcher(early_return=False)
        async def my_coroutine(...):
            ...

        result = my_coroutine(...)  # Blocking call
        ```

        Coroutine usage (returns an awaitable Future):
        ```
        @AsyncDispatcher(return_awaitable=True)
        async def my_coroutine(...):
            ...

        result = await my_coroutine(...)  # Wait for the result to be ready
        ```

        Parameters
        ----------
        loop : LoopID, optional (default: None)
            The event loop to be used, by default get the current event loop.
        early_return : bool, optional (default: True)
            Return the coroutine as a concurrent Future before it is done.
        return_awaitable : bool, optional (default: False)
            Return the coroutine as an awaitable (asyncio) Future instead of a
            concurrent Future. Idenpendently of the value of `early_return`.
        """
        self._loop = self.get_event_loop(loop)
        self._early_return = early_return
        self._return_awaitable = return_awaitable

    @typing.overload
    def __call__(
        self: AsyncDispatcher[typing.Awaitable[_T]],
        async_func: typing.Callable[_P, typing.Awaitable[_T]],
    ) -> typing.Callable[_P, typing.Awaitable[_T]]: ...

    @typing.overload
    def __call__(
        self: AsyncDispatcher[DispatcherFuture[_T]],
        async_func: typing.Callable[_P, typing.Awaitable[_T]],
    ) -> typing.Callable[_P, DispatcherFuture[_T]]: ...

    @typing.overload
    def __call__(
        self: AsyncDispatcher[_T],
        async_func: typing.Callable[_P, typing.Awaitable[_T]],
    ) -> typing.Callable[_P, _T]: ...

    def __call__(
        self,
        async_func: typing.Callable[_P, typing.Awaitable[_T]],
    ) -> typing.Callable[
        _P,
        typing.Union[_T, DispatcherFuture[_T], typing.Awaitable[_T]],  # noqa: UP007
    ]:
        """
        Run the coroutine in the event loop.

        Parameters
        ----------
        *args : tuple
            The positional arguments to be passed to the coroutine.
        **kwargs : dict
            The keyword arguments to be passed to the coroutine.

        Returns
        -------
        concurrent.Future or asyncio.Future or result of the coroutine

        Raises
        ------
        TypeError
            If the function is not a coroutine function.
        """
        if not asyncio.iscoroutinefunction(async_func):
            msg = f"{async_func} is not a coroutine function"
            raise TypeError(msg)

        @functools.wraps(async_func)
        def wrapper(
            *args: _P.args, **kwargs: _P.kwargs,
        ) -> typing.Union[_T, DispatcherFuture[_T], typing.Awaitable[_T]]:  # noqa: UP007
            task = run_coroutine_threadsafe(
                async_func(*args, **kwargs),
                loop=self._loop,
            )
            if self._return_awaitable:
                return asyncio.wrap_future(
                    task, loop=asyncio.get_running_loop(),
                )

            if self._early_return:
                AsyncDispatcher._running_tasks.append(task)
                task.add_done_callback(self._callback_task_done)
                return task
            return task.result()

        return wrapper

    @staticmethod
    def _callback_task_done(future: Future):
        AsyncDispatcher._running_tasks.remove(future)
        with contextlib.suppress(asyncio.CancelledError, CancelledError):
            if (exception := future.exception()) is not None:
                raise exception

    @classmethod
    def get_event_loop(
        cls,
        loop_id: LoopID | None = None,
    ) -> asyncio.AbstractEventLoop:
        """Get the event loop to run the coroutine.

        If the loop is not running, it will be started in a new thread and
        managed by the AsyncDispatcher.

        Parameters
        ----------
        loop_id : LoopID, optional (default: None)
            The event loop to be used, by default gets the current thread event
            loop.

        Notes
        -----
        * If a hashable is provided, it will be used to identify the loop in
          the AsyncDispatcher.
        * If an event loop is provided, it will be used as the event loop in
          the AsyncDispatcher.

        Returns
        -------
        AbstractEventLoop
            The event loop to be used.
        """
        loop, loop_id = cls._fetch_event_loop(loop_id)

        try:
            if loop.is_running():
                return loop
        except RuntimeError:
            _logger.exception(
                "Failed to check if the loop is running, defaulting to the "
                "current loop.",
            )
            return asyncio.get_event_loop()

        with cls.__rlock:
            # Re-check, perhaps it was created in the meantime...
            if loop_id not in cls.__running_threads:
                cls.__run_loop(loop_id, loop)
                if loop_id is None:
                    asyncio.set_event_loop(loop)

        return loop

    @classmethod
    def _fetch_event_loop(
        cls,
        loop_id: LoopID | None = None,
    ) -> tuple[asyncio.AbstractEventLoop, typing.Hashable | None]:
        """Get the event loop and its hashable id."""
        if loop_id is None:
            with contextlib.suppress(RuntimeError):
                return asyncio.get_running_loop(), None
        elif isinstance(loop_id, asyncio.AbstractEventLoop):
            return loop_id, hash(loop_id)

        running_thread = cls.__running_threads.get(loop_id)
        if running_thread is not None:
            return running_thread.loop, loop_id

        return asyncio.new_event_loop(), loop_id

    @classmethod
    def __run_loop(
        cls, loop_id: typing.Hashable, loop: asyncio.AbstractEventLoop,
    ):
        if loop_id not in cls.__running_threads:
            with cls.__rlock:
                if loop_id not in cls.__running_threads:
                    _patch_loop_as_reentrant(loop)  # ipykernel compatibility
                    cls.__running_threads[loop_id] = _LoopRunner(loop_id, loop)
                    cls.__running_threads[loop_id].start()

    @staticmethod
    @atexit.register
    def close():
        """Close the thread pool."""
        if AsyncDispatcher.__closed:
            return
        AsyncDispatcher.cancel_all()
        AsyncDispatcher.join()
        AsyncDispatcher.__closed = True

    @classmethod
    def cancel_all(cls):
        """Cancel all running tasks."""
        for task in cls._running_tasks:
            task.cancel()

    @classmethod
    def join(cls, timeout: float | None = None):
        """Close all running loops and join the threads."""
        for loop_id in list(cls.__running_threads.keys()):
            cls._stop_running_loop(loop_id, timeout)

    @classmethod
    def _stop_running_loop(cls, loop_id: LoopID, timeout: float | None = None):
        runner = cls.__running_threads.pop(loop_id, None)

        if runner is None:
            return

        runner.join(timeout)

    @staticmethod
    def QtSlot(func: typing.Callable[_P, None]) -> typing.Callable[_P, None]:  # noqa: N802
        """Mark a function to be executed inside the main qt loop.

        Set the `DispatcherFuture.QT_SLOT_ATTRIBUTE` attribute to the function
        to mark it as a slot to be executed in the main Qt loop.

        Parameters
        ----------
        func : Callable
            The function to be marked.

        Returns
        -------
        Callable
            The marked function.
        """
        setattr(func, DispatcherFuture.QT_SLOT_ATTRIBUTE, True)
        return func


class _LoopRunner(threading.Thread):
    """A task runner that runs an asyncio event loop on a background thread."""

    def __init__(
        self, loop_id: typing.Hashable, loop: asyncio.AbstractEventLoop,
    ):
        super().__init__(daemon=True, name=f"AsyncDispatcher-{loop_id}")
        self.__loop = loop
        self.__loop_stopped = threading.Event()

    @property
    def loop(self):
        return self.__loop

    def run(self):
        asyncio.set_event_loop(self.__loop)
        try:
            self.__loop.run_forever()
        finally:
            self.__loop.close()
            self.__loop_stopped.set()

    def stop(self):
        self.__loop.call_soon_threadsafe(self.__loop.stop)

    def join(self, timeout: float | None = None):
        if not self.__loop_stopped.is_set():
            self.stop()
            self.__loop_stopped.wait(timeout)
        super().join(timeout)


# ruff: noqa: SLF001
# TODO(hlouzada): refactor this function to reduce its complexity
def _patch_loop_as_reentrant(loop):  # noqa: C901, PLR0915
    """
    Patch an event loop in order to make it reentrant.

    This is a simplified version of the 'nest_asyncio'.

    Parameters
    ----------
    loop : AbstractEventLoop
        The event loop to be patched.

    Raises
    ------
    TypeError
        If the loop is not an instance of `asyncio.BaseEventLoop`.
    """
    if hasattr(loop, "_nest_patched"):
        """Use same check as asyncio to avoid re-patching."""
        return

    def run_forever(self):
        with manage_run(self), manage_asyncgens(self):
            while True:
                self._run_once()
                if self._stopping:
                    break
        self._stopping = False

    def run_until_complete(self, future):
        with manage_run(self):
            f = asyncio.ensure_future(future, loop=self)
            if f is not future:
                f._log_destroy_pending = False
            while not f.done():
                self._run_once()
                if self._stopping:
                    break
            if not f.done():
                msg = "Event loop stopped before Future completed."
                raise RuntimeError(msg)
            return f.result()

    def _run_once(self):
        """Run handles as they become ready.

        Simplified re-implementation of asyncio's _run_once
        """
        ready = self._ready
        scheduled = self._scheduled
        while scheduled and scheduled[0]._cancelled:
            heappop(scheduled)

        timeout = (
            0
            if ready or self._stopping
            else min(max(scheduled[0]._when - self.time(), 0), 86400)
            if scheduled
            else None
        )
        event_list = self._selector.select(timeout)
        self._process_events(event_list)

        end_time = self.time() + self._clock_resolution
        while scheduled and scheduled[0]._when < end_time:
            handle = heappop(scheduled)
            ready.append(handle)

        for __ in range(len(ready)):
            if not ready:
                break
            handle = ready.popleft()
            if not handle._cancelled:
                # preempt the current task so that that checks in
                # Task.__step do not raise
                curr_task = _current_tasks.pop(self, None)

                try:
                    handle._run()
                finally:
                    # restore the current task
                    if curr_task is not None:
                        _current_tasks[self] = curr_task

        handle = None

    @contextlib.contextmanager
    def manage_run(self):
        """Set up the loop for running."""
        self._check_closed()
        old_thread_id = self._thread_id
        old_running_loop = asyncio.events._get_running_loop()
        try:
            self._thread_id = threading.get_ident()
            asyncio.events._set_running_loop(self)
            self._num_runs_pending += 1
            if self._is_proactorloop and self._self_reading_future is None:
                self.call_soon(self._loop_self_reading)
            yield
        finally:
            self._thread_id = old_thread_id
            asyncio.events._set_running_loop(old_running_loop)
            self._num_runs_pending -= 1
            if (
                self._is_proactorloop
                and self._num_runs_pending == 0
                and self._self_reading_future is not None
            ):
                ov = self._self_reading_future._ov
                self._self_reading_future.cancel()
                if ov is not None:
                    self._proactor._unregister(ov)
                self._self_reading_future = None

    @contextlib.contextmanager
    def manage_asyncgens(self):
        if not hasattr(sys, "get_asyncgen_hooks"):
            # Python version is too old.
            return
        old_agen_hooks = sys.get_asyncgen_hooks()
        try:
            self._set_coroutine_origin_tracking(self._debug)
            if self._asyncgens is not None:
                sys.set_asyncgen_hooks(
                    firstiter=self._asyncgen_firstiter_hook,
                    finalizer=self._asyncgen_finalizer_hook,
                )
            yield
        finally:
            self._set_coroutine_origin_tracking(False)
            if self._asyncgens is not None:
                sys.set_asyncgen_hooks(*old_agen_hooks)

    def _check_running(self):
        """Do not throw exception if loop is already running."""

    if not isinstance(loop, asyncio.BaseEventLoop):
        msg = f"Can't patch loop of type {type(loop)}"
        raise TypeError(msg)

    cls = loop.__class__
    cls.run_forever = run_forever
    cls.run_until_complete = run_until_complete
    cls._run_once = _run_once
    cls._check_running = _check_running
    cls._num_runs_pending = 1 if loop.is_running() else 0
    cls._is_proactorloop = os.name == "nt" and issubclass(
        cls, asyncio.ProactorEventLoop,
    )
    cls._nest_patched = True


class _QCallbackEvent(QEvent):
    """Event to execute a callback in the main Qt loop."""

    def __init__(self, func: typing.Callable):
        super().__init__(QEvent.Type.User)
        self.func = func


class _QCallbackExecutor(QObject):
    """Executor to run callbacks in the main Qt loop."""

    def customEvent(self, e: _QCallbackEvent):  # noqa: N802, PLR6301
        e.func()


class DispatcherFuture(Future, typing.Generic[_T]):
    """Represents the result of an asynchronous computation.

    This class is a subclass of `concurrent.Future` that adds a `connect`
    method to allow attaching callbacks to be executed in the main Qt loop.
    """

    QT_SLOT_ATTRIBUTE = "__dispatch_qt_slot__"

    _callback_executor = _QCallbackExecutor()

    def result(self, timeout: typing.Optional[float] = None) -> _T:  # noqa: UP045
        """
        Return the result of the call that the future represents.

        Parameters
        ----------
        timeout: float | None
            The number of seconds to wait for the result. If None, then wait
            indefinitely.

        Returns
        -------
        DispatchedFuture@_T
            The result of the call that the future represents.

        Raises
        ------
        CancelledError
            If the future was cancelled.

        TimeoutError
            If the future didn't finish executing before the given timeout.

        Exception
            Exception raised by the call that the future represents.
        """  # noqa: DOC502
        return super().result(timeout=timeout)

    def connect(self, fn: typing.Callable[[DispatcherFuture[_T]], None]):
        """Attaches a callable that will be called when the future finishes.

        The callable will be called by a thread in the same process in which
        it was added if the it was not marked with
        `DispatherFuture.QT_SLOT_ATTRIBUTE`.

        If the future has already completed or been
        cancelled then the callable will be called immediately. These
        callables are called in the order that they were added.

        Parameters
        ----------
        fn: Callable
            A callable that will be called with this future's as its only
            argument when the future completes.

        """
        if getattr(fn, self.QT_SLOT_ATTRIBUTE, False):

            def callback(future: DispatcherFuture[_T]):
                e = _QCallbackEvent(lambda: fn(future))
                QCoreApplication.postEvent(self._callback_executor, e)

            self.add_done_callback(callback)  # type: ignore[arg-type]
        else:
            self.add_done_callback(fn)  # type: ignore[arg-type]


def run_coroutine_threadsafe(
    coro: typing.Coroutine[_T, None, _RT], loop: asyncio.AbstractEventLoop,
) -> DispatcherFuture[_RT]:
    """Submit a coroutine object to a given event loop.

    Arguments
    ---------
    coro: Coroutine
        The coroutine object to be submitted.
    loop: AbstractEventLoop
        The event loop to run the coroutine.

    Returns
    -------
    DispatcherFuture
        A future object representing the result of the coroutine.

    Raises
    ------
    TypeError
        If the object is not a coroutine.
    """
    if not asyncio.iscoroutine(coro):
        msg = "A coroutine object is required"
        raise TypeError(msg)
    future = DispatcherFuture()

    def callback():
        try:
            _chain_future(asyncio.ensure_future(coro, loop=loop), future)
        except (SystemExit, KeyboardInterrupt):
            raise
        except BaseException as exc:
            if future.set_running_or_notify_cancel():
                future.set_exception(exc)
            raise

    loop.call_soon_threadsafe(callback)
    return future
