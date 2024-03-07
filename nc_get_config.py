import xml.dom.minidom

from ncclient import manager

from tsn_config_xml import LLDP_FILTER, get_interface_filter


def get_switch_config(ip_address: str, debug: bool = False):
    m = manager.connect(
        host=ip_address, port=830, username="thesis", password="thesis", hostkey_verify=False
    )
    # LLDP CONFIG
    config = None
    config = m.get(filter=LLDP_FILTER)
    # lldp_xmlDom = xml.dom.minidom.parseString(str(config))
    # with open("lldp_config.xml", "w") as f:
    #     f.write(lldp_xmlDom.toprettyxml(indent="  "))

    if debug:
        # FULL CONFIG
        # full_config = m.get_config("running")
        # xmlDom = xml.dom.minidom.parseString(str(full_config))
        # with open("full_config.xml", "w") as f:
        #     f.write(xmlDom.toprettyxml(indent="  "))


        # INTERFACES
        filter = get_interface_filter("sw0p5")
        qbv_config = str(m.get_config("running", filter))
        qbv_xmlDom = xml.dom.minidom.parseString(qbv_config)
        print(qbv_xmlDom.toprettyxml(indent="  "))

        # with open("interface_info.xml", "w") as f:
        #     f.write(qbv_xmlDom.toprettyxml(indent="  "))

    return config


if __name__ == "__main__":
    get_switch_config("169.254.9.19", debug=True)
