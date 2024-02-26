from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Union
from collections import OrderedDict
import json

import xmltodict

REPLY_TAG = "nc:rpc-reply"
DATA_TAG = "data"


class RemoteConnection(BaseModel):
    time_mark: str = Field(alias="time-mark")
    remote_index: str = Field(alias="remote-index")
    chassis_id_subtype: str = Field(alias="chassis-id-subtype")
    chassis_id: str = Field(alias="chassis-id")
    port_id: str = Field(alias="port-id")
    port_id_subtype: str = Field(alias="port-id-subtype")
    port_desc: Optional[str] = Field(alias="port-desc", default=None)
    system_name: str = Field(alias="system-name")
    system_description: Optional[str] = Field(alias="system-description", default=None)
    system_capabilities_supported: str = Field(alias="system-capabilities-supported")
    system_capabilities_enabled: str = Field(alias="system-capabilities-enabled")
    management_address: Optional[List] = Field(alias="management-address", default=None)


class CNCPort(BaseModel):
    name: str
    dest_mac_address: str = Field(alias="dest-mac-address")
    management_address_tx_port: Dict = Field(alias="management-address-tx-port")
    port_id: str = Field(alias="port-id")
    port_id_subtype: str = Field(alias="port-id-subtype")
    port_desc: str = Field(alias="port-desc")
    tx_statistics: Dict = Field(alias="tx-statistics")
    rx_statistics: Dict = Field(alias="rx-statistics")
    remote_systems_data: Optional[Union[List[RemoteConnection], RemoteConnection]] = Field(
        alias="remote-systems-data", default=None
    )


def _get_element(ele: Dict, attrs: List[str]):
    if len(attrs) == 0:
        return ele
    found_element = ele[attrs[0]]
    attrs.pop(0)

    return _get_element(found_element, attrs)


def extract_ports_from_lldp(port: OrderedDict):
    cnc_port = CNCPort.model_validate(port)
    name = cnc_port.name

    connections = cnc_port.remote_systems_data
    connected_port = None

    if connections:
        conn: RemoteConnection = connections[0] if (type(connections) is list) else connections  # type: ignore[union-attr, assignment]
        connected_port = conn.port_desc or conn.port_id
        connected_address = conn.management_address
        # print(connected_address)

    return name, connected_port


def handle_config(data: str, target_element: str):
    ports = {}

    attr_list = target_element.split(".")
    config_data = xmltodict.parse(data)
    # print(json.dumps(config_data))
    found = _get_element(config_data[REPLY_TAG][DATA_TAG], attr_list.copy())
    if "port" in attr_list:
        for found_port in found:
            port_name, port_connection = extract_ports_from_lldp(found_port)
            ports[port_name] = port_connection

            # print(f"LLDP return port: {port_name} - {port_connection}\n")

    return ports


# handle_config("", "lldp.port")
