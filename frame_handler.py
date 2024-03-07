import socket

from loguru import logger
from scapy.contrib.lldp import LLDPDUManagementAddress, LLDPDUSystemDescription
from scapy.packet import Packet

from nc_get_config import get_switch_config
from network_map import NetworkMap, Switch, SwitchNode
from process_switch_config import handle_config

LINK_DELAY = 420000


class FrameHandler:
    def __init__(self, nw_map: NetworkMap) -> None:
        self.nw_map = nw_map

    def update_nw_map(self, ip: str, switch_name: str):
        new_switch = Switch(name=switch_name, ip_address=ip)
        # self.nw_map.add_switch(new_switch)

        new_switch_node = SwitchNode(switch=new_switch, link_delay_to_prev=LINK_DELAY)
        self.nw_map.add_switch_and_node(new_switch, new_switch_node)
        ###

        # Send NETCONF request to get switch information
        lldp_config = get_switch_config(ip)

        # extract port information from switch config
        found_ports = handle_config(str(lldp_config), "lldp.port")
        for port_name, connection in found_ports.items():
            self.nw_map.add_port(
                port_name=port_name,
                switch=new_switch,
                connection_port=connection,
            )

    def get_frame_info(self, frame: Packet):
        switch_name, switch_ip = "", ""

        if LLDPDUManagementAddress in frame.layers():
            enconded_ip = frame[LLDPDUManagementAddress].management_address
            switch_ip = socket.inet_ntoa(enconded_ip)
        if LLDPDUSystemDescription in frame.layers():
            name = frame[LLDPDUSystemDescription].description
            switch_name = bytes(name).decode()

        logger.success(f"Getting LLDP frame of {switch_ip=}, updating network map")

        self.update_nw_map(switch_ip, switch_name)

        logger.info(f"Network map: {self.nw_map}")
