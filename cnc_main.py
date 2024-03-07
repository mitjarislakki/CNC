import asyncio

from loguru import logger

from bridge_discovery.frame_handler import FrameHandler
from bridge_discovery.sniff_lldp import sniff_lldp_frame
from network_map import init_nw_map
from traffic_shaper import shape_traffic


async def main():
    nw_map = init_nw_map()

    handler = FrameHandler(nw_map)

    ## Waiting for LLDP frame from switches, update NW map in the background
    sniffing_task = asyncio.create_task(sniff_lldp_frame(handler))

    traffic_shaping_task = asyncio.create_task(shape_traffic(nw_map))

    await asyncio.gather(*[sniffing_task, traffic_shaping_task])


asyncio.run(main())
