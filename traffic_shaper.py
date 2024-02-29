from nc_edit_config import edit_switch_schedule
from tsn_config_xml import get_qbv_config
from network_map import get_nw_map, Switch
import asyncio

CYCLE_TIME = 800
RESIDENCE_TIME = 0
LINK_DELAY = 0


def calculate_schedule(switch: Switch):
    # TODO: different NWMap data structure for this calculation
    print(f"Shaping traffic for {switch.ip_address}\n")

    total_residence_time = RESIDENCE_TIME
    total_link_delay = LINK_DELAY

    offset = total_residence_time + total_link_delay

    cycle_time = CYCLE_TIME
    return cycle_time, offset


async def shape_traffic(nw_map):
    nw_map_is_complete = True

    # poll until nw_map is complete
    while nw_map is None or (not nw_map_is_complete):
        await asyncio.sleep(5)
        nw_map = get_nw_map()

    while True:
        # calculate new schedule if nw map changes
        if nw_map.map_has_changed:
            switches = nw_map.switches
            for switch in switches:
                # 3. compute schedule for this switch
                cycle_time, offset = calculate_schedule(switch)
                qbv_config = get_qbv_config(cycle_time=cycle_time, off_set=offset)

                # 4. send schedule to switches
                edit_switch_schedule(switch.ip_address, qbv_config)

            nw_map.finish_processing_map()

        await asyncio.sleep(5)
