from datetime import datetime

import pytest

from ..deprecated.async_timer import AsyncTimer


@pytest.mark.asyncio
async def test_timer():
    timeout = 1.2  # seconds
    start = datetime.now()

    # end = None

    def cb():
        print("Starting callback")
        global end
        end = datetime.now()
        print(end)

    a_timer = AsyncTimer(timeout=timeout, ontimeout=cb)
    a_timer.start()
    await a_timer.wait()

    total_time = round((end - start).total_seconds(), 1)

    # give a 0.2 window within which we can call it valid, due to the async nature of this test
    assert timeout <= total_time <= timeout + 0.2

    assert False
