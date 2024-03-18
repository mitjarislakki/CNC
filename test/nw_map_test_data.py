from network_map import NetworkMap, Switch, SwitchNode

SWITCHES: list[dict] = [
    {
        "name": "B&R",
        "ip": "169.254.9.19",
        "ports": {"sw0p1": "Port 1", "sw0p2": None, "sw0p3": "GigabitEthernet1 2", "sw0p4": None},
    },
    {
        "name": "Kon",
        "ip": "169.254.9.26",
        "ports": {
            "GigabitEthernet1 1": None,
            "GigabitEthernet1 2": "sw0p3",
            "GigabitEthernet1 3": None,
            "GigabitEthernet1 4": None,
            "GigabitEthernet1 5": None,
            "GigabitEthernet1 6": None,
            "GigabitEthernet2 7": None,
            "GigabitEthernet2 8": None,
        },
    },
    {
        "name": "TSwitch",
        "ip": "158.27.110.30",
        "ports": {"Port 1": "sw0p1", "Port 2": None},
    },
]


def init_nw_map() -> NetworkMap:
    _nw_map = NetworkMap()

    def _update_nw_map(switch: Switch, ports: dict[str, any]):
        new_node = SwitchNode(switch=switch, link_delay_to_prev=400)
        _nw_map.add_switch_and_node(switch, new_node)
        for port_name, connection in ports.items():
            _nw_map.add_port(port_name=port_name, switch=switch, connection_port=connection)

    for switch in SWITCHES:
        # pseudo update
        new_switch_name = switch.get("name", "Pseudo name")
        ip = switch.get("ip", "")
        ports = switch.get("ports")
        new_swi = Switch(name=new_switch_name, ip_address=ip)
        if ports:
            _update_nw_map(new_swi, ports)

    return _nw_map
