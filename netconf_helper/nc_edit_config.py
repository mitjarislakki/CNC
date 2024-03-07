import xml.dom.minidom

from ncclient import manager

from netconf_helper.tsn_config_xml import get_gcl, get_interface_filter, get_qbv_config


def edit_config_req(manager: manager.Manager, config, filter=None):
    manager.edit_config(target="running", config=config, test_option="test-then-set")
    # m.commit() # only needed if target is candidate

    if filter:
        get_config = manager.get_config("running", filter)
        dom = xml.dom.minidom.parseString(str(get_config))
        print(dom.toprettyxml(indent="  "))


def edit_switch_schedule(ip_address: str, config_param):
    m = manager.connect(
        host=ip_address, port=830, username="thesis", password="thesis", hostkey_verify=False
    )

    edit_config_req(m, config_param)


def get_outgress_port_gcl(test_case: int):
    if test_case == 1:
        pair1_outport = get_gcl(bm=[255], val=[10000000])
        pair2_outport = get_gcl(bm=[255], val=[5000000])
    elif test_case == 2:
        pair1_outport = get_gcl(bm=[255], val=[5000000])
        pair2_outport = get_gcl(bm=[255], val=[10000000])
    elif test_case == 3:
        pair1_outport = get_gcl(bm=[253, 64], val=[2000000, 8000000])
        pair2_outport = get_gcl(bm=[253, 64], val=[2000000, 8000000])
    else:
        pair1_outport = []
        pair2_outport = []

    return {"pair1_outport": pair1_outport, "pair2_outport": pair2_outport}


if __name__ == "__main__":
    with manager.connect(host="169.254.9.19", port=830, username="thesis", password="thesis") as m:
        cycle_time = 100
        control_list = get_outgress_port_gcl(test_case=3)
        qbv_config = get_qbv_config(cycle_time=cycle_time, control_list=control_list)
        # print(qbv_config)

        interf_filter = get_interface_filter("sw0p5")
        edit_config_req(m, qbv_config, interf_filter)
