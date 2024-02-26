from network_map import init_nw_map, get_nw_map
from frame_handler import FrameHandler
from sniff_lldp import sniff_lldp_frame
import asyncio

from loguru import logger
from traffic_shaper import shape_traffic


async def main():
    nw_map = init_nw_map()

    handler = FrameHandler(nw_map)

    ## Waiting for LLDP frame from switches, update NW map in the background
    sniffing_task = asyncio.create_task(sniff_lldp_frame(handler))

    traffic_shaping_task = asyncio.create_task(shape_traffic(nw_map))

    group = await asyncio.gather(*[sniffing_task, traffic_shaping_task])

    ## wait for the coroutine to finish (~ running it in the background; BLOCKING!)
    # await group

    # 2. determine latency requirement? -> hard-coded latency for TSN flow

    # 3. TODO: (create Task that) read NW map and compute route schedule
    """
    Result: for ~this~ flow:
        flow ID: OK
        destination MAC (talker & listener) OK
        CoS (PCP value: 7): ??

        Period cycle time (hardcoded?: 100ms) OK
        talker transmit window: ??
        receiver window:
    """


asyncio.run(main())
