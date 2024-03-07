import asyncio

from nc_edit_config import edit_switch_schedule
from network_map import SwitchNode, get_nw_map
from tsn_config_xml import get_qbv_config

CYCLE_TIME = 800
LINK_DELAY = 420000  # 0.42ms


def calc_egress_offset(node: SwitchNode) -> int:
    egress_offset = node.latency_to_prev  # link delay + residence time
    if node.previous:
        return calc_egress_offset(node.previous) + egress_offset
    else:
        return egress_offset


def calculate_schedule_for_node(node: SwitchNode):
    print(f"Shaping traffic for {node.switch.ip_address}\n")

    offset_egress = calc_egress_offset(node)
    switch_residence_time = node.switch.residence_time
    offset_ingress = offset_egress - switch_residence_time

    cycle_time = CYCLE_TIME
    return cycle_time, offset_ingress, offset_egress


async def shape_traffic(nw_map):
    nw_map_is_complete = True

    # poll until nw_map is complete
    while nw_map is None or (not nw_map_is_complete):
        await asyncio.sleep(5)
        nw_map = get_nw_map()

    while True:
        # calculate new schedule if nw map changes
        if nw_map.map_has_changed:
            switch_nodes = nw_map.switch_nodes
            for node in switch_nodes:
                # 3. compute schedule for this switch
                cycle_time, offset_ingress, offset_egress = calculate_schedule_for_node(node)
                qbv_config = get_qbv_config(
                    cycle_time=cycle_time,
                    offset_ingress=offset_ingress,
                    offset_egress=offset_egress,
                )

                # 4. send schedule to switches
                # edit_switch_schedule(node.switch.ip_address, qbv_config)

            nw_map.finish_processing_map()

        await asyncio.sleep(5)
