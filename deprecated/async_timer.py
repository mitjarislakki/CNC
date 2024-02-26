import asyncio
import contextlib
from asyncio.tasks import Task
from typing import Callable, Optional, List
from loguru import logger


TIMEOUT = 120


class AsyncTimer:
    def __init__(self, ontimeout: Callable[[], None], timeout: float = TIMEOUT):
        self.timeout = timeout
        self.ontimeout = ontimeout
        self.timer_task: Optional[Task] = None

    def pr(self, val):
        print(val)

    async def _timer(self) -> None:
        logger.warning("Sleeping")
        await asyncio.sleep(self.timeout)
        logger.warning(f"EXPIRES \n")
        self.ontimeout()
        # self.pr("WHY U DONT WORK")

    def start(self) -> None:
        print("\n Starting timer")
        if self.timer_task is None or self.timer_task.done() or self.timer_task.cancelled():
            # loop = asyncio.get_event_loop()
            self.timer_task = asyncio.create_task(self._timer())

    async def restart(self) -> None:
        with contextlib.suppress(asyncio.CancelledError):
            self.cancel()
            if self.timer_task is not None:
                await self.timer_task
        self.timer_task = asyncio.create_task(self._timer())

    def cancel(self) -> None:
        if self.timer_task:
            self.timer_task.cancel()

    async def wait(self) -> None:
        if self.timer_task:
            await asyncio.wait({self.timer_task})


class GlobalTimers:
    timers: List[Task]
