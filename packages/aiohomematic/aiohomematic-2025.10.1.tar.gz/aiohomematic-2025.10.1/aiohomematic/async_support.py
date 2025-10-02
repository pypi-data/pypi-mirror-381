# SPDX-License-Identifier: MIT
# Copyright (c) 2021-2025 Daniel Perna, SukramJ
"""Module with support for loop interaction."""

from __future__ import annotations

import asyncio
from collections.abc import Callable, Collection, Coroutine
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures._base import CancelledError
from functools import wraps
import logging
from time import monotonic
from typing import Any, Final, cast

from aiohomematic.const import BLOCK_LOG_TIMEOUT
from aiohomematic.exceptions import AioHomematicException
from aiohomematic.support import debug_enabled, extract_exc_args

_LOGGER: Final = logging.getLogger(__name__)


class Looper:
    """Helper class for event loop support."""

    def __init__(self) -> None:
        """Init the loop helper."""
        self._tasks: Final[set[asyncio.Future[Any]]] = set()
        self._loop = asyncio.get_event_loop()

    async def block_till_done(self, wait_time: float | None = None) -> None:
        """
        Block until all pending work is done.

        If wait_time is set, stop waiting after the given number of seconds and log remaining tasks.
        """
        # To flush out any call_soon_threadsafe
        await asyncio.sleep(0)
        start_time: float | None = None
        deadline: float | None = (monotonic() + wait_time) if wait_time is not None else None
        current_task = asyncio.current_task()
        while tasks := [task for task in self._tasks if task is not current_task and not cancelling(task)]:
            # If we have a deadline and have exceeded it, log remaining tasks and break
            if deadline is not None and monotonic() >= deadline:
                for task in tasks:
                    _LOGGER.warning("Shutdown timeout reached; task still pending: %s", task)
                break

            await self._await_and_log_pending(tasks)

            if start_time is None:
                # Avoid calling monotonic() until we know
                # we may need to start logging blocked tasks.
                start_time = 0
            elif start_time == 0:
                # If we have waited twice then we set the start
                # time
                start_time = monotonic()
            elif monotonic() - start_time > BLOCK_LOG_TIMEOUT:
                # We have waited at least three loops and new tasks
                # continue to block. At this point we start
                # logging all waiting tasks.
                for task in tasks:
                    _LOGGER.debug("Waiting for task: %s", task)

    async def _await_and_log_pending(self, pending: Collection[asyncio.Future[Any]]) -> None:
        """Await and log tasks that take a long time."""
        wait_time = 0
        while pending:
            _, pending = await asyncio.wait(pending, timeout=BLOCK_LOG_TIMEOUT)
            if not pending:
                return
            wait_time += BLOCK_LOG_TIMEOUT
            for task in pending:
                _LOGGER.debug("Waited %s seconds for task: %s", wait_time, task)

    def create_task(self, target: Coroutine[Any, Any, Any], name: str) -> None:
        """Add task to the executor pool."""
        try:
            self._loop.call_soon_threadsafe(self._async_create_task, target, name)
        except CancelledError:
            _LOGGER.debug(
                "create_task: task cancelled for %s",
                name,
            )
            return

    def _async_create_task[R](self, target: Coroutine[Any, Any, R], name: str) -> asyncio.Task[R]:
        """Create a task from within the event_loop. This method must be run in the event_loop."""
        task = self._loop.create_task(target, name=name)
        self._tasks.add(task)
        task.add_done_callback(self._tasks.remove)
        return task

    def run_coroutine(self, coro: Coroutine, name: str) -> Any:
        """Call coroutine from sync."""
        try:
            return asyncio.run_coroutine_threadsafe(coro, self._loop).result()
        except CancelledError:  # pragma: no cover
            _LOGGER.debug(
                "run_coroutine: coroutine interrupted for %s",
                name,
            )
            return None

    def async_add_executor_job[T](
        self,
        target: Callable[..., T],
        *args: Any,
        name: str,
        executor: ThreadPoolExecutor | None = None,
    ) -> asyncio.Future[T]:
        """Add an executor job from within the event_loop."""
        try:
            task = self._loop.run_in_executor(executor, target, *args)
            self._tasks.add(task)
            task.add_done_callback(self._tasks.remove)
        except (TimeoutError, CancelledError) as err:  # pragma: no cover
            message = f"async_add_executor_job: task cancelled for {name} [{extract_exc_args(exc=err)}]"
            _LOGGER.debug(message)
            raise AioHomematicException(message) from err
        return task

    def cancel_tasks(self) -> None:
        """Cancel running tasks."""
        for task in self._tasks.copy():
            if not task.cancelled():
                task.cancel()


def cancelling(task: asyncio.Future[Any]) -> bool:
    """Return True if task is cancelling."""
    return bool((cancelling_ := getattr(task, "cancelling", None)) and cancelling_())


def loop_check[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Annotation to mark method that must be run within the event loop."""

    _with_loop: set = set()

    @wraps(func)
    def wrapper_loop_check(*args: P.args, **kwargs: P.kwargs) -> R:
        """Wrap loop check."""
        return_value = func(*args, **kwargs)

        try:
            asyncio.get_running_loop()
            loop_running = True
        except Exception:
            loop_running = False

        if not loop_running and func not in _with_loop:
            _with_loop.add(func)
            _LOGGER.warning("Method %s must run in the event_loop. No loop detected.", func.__name__)

        return return_value

    setattr(func, "_loop_check", True)
    return cast(Callable[P, R], wrapper_loop_check) if debug_enabled() else func
