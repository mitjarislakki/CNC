from scapy.packet import Packet
from scapy.sendrecv import sniff
from scapy.contrib.lldp import LLDPDU, LLDPDUManagementAddress, LLDPDUSystemDescription
from typing import List
from scapy.base_classes import SetGen
import socket

INTERF = "enxa0cec8877051"


def _get_fields(frame: Packet):
    print(f"\n{frame.name}")
    for desc in frame.fields_desc:
        print(f"\nFrame's field: {desc}, {type(desc)}\n")

        field_value = frame.getfieldval(desc.name)
        print(f"{field_value=}")

        fvalue_gen = SetGen(field_value, _iterpacket=0)
        print(fvalue_gen.values)
        if isinstance(field_value, Packet) or (
            desc.islist and desc.holds_packets and isinstance(field_value, list)
        ):
            for fval in fvalue_gen:
                print(f"\ninner value {fval}, {type(fval)}\n")
                _get_fields(fval)


def get_packet_layers(packet: Packet):
    counter = 0
    while True:
        layer = packet.getlayer(counter)
        if layer is None:
            break

        yield layer
        counter += 1


def get_lldp() -> List[Packet]:
    switch_lldp = []

    def _stop_filter(frame: Packet):
        if frame.haslayer(LLDPDU):
            frame_content = frame.show(dump=True)
            if "switch" in frame_content.lower():
                if __name__ == "__main__":
                    for layer in get_packet_layers(frame):
                        _get_fields(layer)
                    print(frame_content)
                switch_lldp.append(frame)
                return True

    lldp_responses = sniff(
        iface=INTERF,
        stop_filter=_stop_filter,
        timeout=45,
        # prn=lambda x: x.summary(),
    )

    return switch_lldp


def decode_ip(encoded_ip: bytes):
    address = socket.inet_ntoa(encoded_ip)
    return address


def get_lldp_info():
    switch_lldp = get_lldp()[0]
    switch_name, switch_ip = "", ""
    if LLDPDUManagementAddress in switch_lldp.layers():
        enconded_ip = switch_lldp[LLDPDUManagementAddress].management_address
        switch_ip = decode_ip(enconded_ip)
    if LLDPDUSystemDescription in switch_lldp.layers():
        name = switch_lldp[LLDPDUSystemDescription].description
        switch_name = bytes(name).decode()
    return switch_name, switch_ip


if __name__ == "__main__":
    print(get_lldp_info())
