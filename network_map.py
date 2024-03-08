from typing import List, Optional

from pydantic import BaseModel, model_validator

RESIDENCE_TIME = 800  # in nanosec


class Switch(BaseModel):
    name: str
    ip_address: str
    residence_time: int = RESIDENCE_TIME
    connections: List["Switch"] = []


class Port(BaseModel):
    name: str
    switch: Switch
    connection: Optional[str] = None


class SwitchNode(BaseModel):
    switch: Switch
    link_delay_to_prev: int
    previous: Optional["SwitchNode"] = None

    @property
    def latency_to_prev(self):
        # link delay + residence time
        return self.link_delay_to_prev + self.switch.residence_time


def calculate_offset(node: SwitchNode):
    ingress_offset = node.latency_to_prev
    if node.previous:
        return calculate_offset(node.previous)
    else:
        return ingress_offset


class NetworkMap(BaseModel):
    switch_nodes: List[SwitchNode] = []
    switches: List[Switch] = []
    ports: List[Port] = []
    map_has_changed: bool = False

    # VALIDATOR AND HELPER

    @model_validator(mode="after")
    def check_switch(self) -> "NetworkMap":
        for port in self.ports:
            if port.switch not in [switch.name for switch in self.switches]:
                raise ValueError("port's switch is not available")
        return self

    def _port_exists(self, port: Port) -> Optional[Port]:
        for p in self.ports:
            if p.name == port.name and p.switch == port.switch:
                return p

        return None

    def _switch_exist(self, switch: Switch):
        if switch.ip_address in [sw.ip_address for sw in self.switches]:
            return True
        return False

    def _connect_switch(self, new_port: Port):
        for p in self.ports:
            if p.name == new_port.connection:
                p.switch.connections.append(new_port.switch)
                new_port.switch.connections.append(p.switch)
                return

    def _get_node_from_switch(self, switch: Switch) -> Optional[SwitchNode]:
        for node in self.switch_nodes:
            if node.switch.name == switch.name:
                return node
        return None

    def _connect_switch_node(self, new_node: SwitchNode):
        # Pseudo
        if len(self.switch_nodes) > 0:
            self.switch_nodes[0].previous = new_node
            return

    def __str__(self):
        output = "Network map: \n"
        for switch in self.switches:
            output += f"{switch.name=} "
            output += f"{switch.ip_address=}\n"

        for p in self.ports:
            if p.connection:
                output += f"{p.name=} connected to {p.connection}\n"
            else:
                output += f"{p.name}; "
        return output

    # MODIFY NETWORK

    def add_switch_node(self, new_switch: SwitchNode):
        self._connect_switch_node(new_switch)
        self.switch_nodes.append(new_switch)

    def add_switch(self, new_switch: Switch):

        self.switches.append(new_switch)
        # print(f"Switch {self.map_has_changed}")

    def add_switch_and_node(self, new_switch: Switch, new_node: SwitchNode):
        if self._switch_exist(new_switch):
            return
        self.add_switch(new_switch)
        self.add_switch_node(new_node)
        self.map_has_changed = True

    def add_port(self, port_name: str, switch: Switch, connection_port: Optional[str]):
        new_port = Port(name=port_name, switch=switch)

        if existing_port := self._port_exists(new_port):
            if existing_port.connection == connection_port:
                return
            # TODO: update the port's connection works here? -> write test
            existing_port.connection = connection_port
            self.map_has_changed = True
            return

        if connection_port:
            new_port.connection = connection_port
            self._connect_switch(new_port)

        self.ports.append(new_port)
        self.map_has_changed = True

    def finish_processing_map(self):
        self.map_has_changed = False


_nw_map = None


def init_nw_map() -> NetworkMap:
    global _nw_map
    _nw_map = NetworkMap()

    return _nw_map


def get_nw_map():
    global _nw_map
    return _nw_map
