from ncclient import manager
import xml.dom.minidom
from config_params import (
    BRIDGE_CONFIG,
    BRIDGE_FILTER,
    QBV_CONFIG,
    LLDP_CONFIG,
    LLDP_FILTER,
)
from tsn_config_xml import get_qbv_config


def edit_config_req(manager: manager.Manager, config, filter=None):
    manager.edit_config(target="running", config=config, test_option="test-then-set")
    # m.commit() # only needed if target is candidate

    if filter:
        get_config = manager.get_config("running", filter)
        dom = xml.dom.minidom.parseString(str(get_config))
        print(dom.toprettyxml(indent="  "))


def edit_switch_schedule(ip_address: str, config_param=QBV_CONFIG):
    m = manager.connect(
        host=ip_address, port=830, username="thesis", password="thesis", hostkey_verify=False
    )

    edit_config_req(m, config_param)


if __name__ == "__main__":
    with manager.connect(host="169.254.9.19", port=830, username="thesis", password="thesis") as m:
        """edit bridge config, frames with VLANID 1100 are forwarded to all port"""
        # edit_config_req(m, BRIDGE_CONFIG, BRIDGE_FILTER)

        """ edit QBV: cycle time = 1ms;
            on all ports queue 7 open for 600micros, 0-6: 400micros
            """
        edit_config_req(m, get_qbv_config())

        """ apply the changes """
        # edit_config_req(m, OPERATION)

        # # ! modification not supported
        # edit_config_req(m, LLDP_CONFIG, LLDP_FILTER)
