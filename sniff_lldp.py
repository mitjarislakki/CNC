from scapy.packet import Packet
from scapy.sendrecv import sniff, AsyncSniffer
from scapy.contrib.lldp import LLDPDU
from scapy.base_classes import SetGen
import asyncio

from frame_handler import FrameHandler

INTERF = "enxa0cec8877051"

# handler = FrameHandler()


def _get_fields(frame: Packet):
    print(f"\n# {frame.name}")
    for desc in frame.fields_desc:
        print(f"\nFrame's field: {desc}\n")

        field_value = frame.getfieldval(desc.name)
        print(f"{field_value=}")

        fvalue_gen = SetGen(field_value, _iterpacket=0)
        if isinstance(field_value, Packet) or (
            desc.islist and desc.holds_packets and isinstance(field_value, list)
        ):
            for fval in fvalue_gen:
                print(f"\nInner value {fval}, {type(fval)}\n")
                _get_fields(fval)


def get_packet_layers(packet: Packet):
    counter = 0
    while True:
        layer = packet.getlayer(counter)
        if layer is None:
            break

        yield layer
        counter += 1


# async def sniff_lldp_frame(handler: FrameHandler):
#     def _process_lldp(frame: Packet):
#         if frame.haslayer(LLDPDU):
#             frame_content = frame.show(dump=True)
#             if "switch" in frame_content.lower():
#                 if __name__ == "__main__":
#                     for layer in get_packet_layers(frame):
#                         _get_fields(layer)
#                     print(frame_content)
#                 handler.get_frame_info(frame)

#     sniffer = AsyncSniffer(
#         iface=INTERF,
#         prn=_process_lldp,
#         store=False,
#     )
#     sniffer.start()


#     while True:
#         await asyncio.sleep(2)


async def sniff_lldp_frame(handler: FrameHandler):
    def _process_lldp(frame: Packet):
        if frame.haslayer(LLDPDU):
            frame_content = frame.show(dump=True)
            if "switch" in frame_content.lower():
                if __name__ == "__main__":
                    for layer in get_packet_layers(frame):
                        _get_fields(layer)
                    print(frame_content)
                handler.get_frame_info(frame)

    def _stop_filter(frame: Packet):
        if frame.haslayer(LLDPDU):
            frame_content = frame.show(dump=True)
            if "switch" in frame_content.lower():
                return True

    # sniff(iface=INTERF, prn=_process_lldp)

    while True:
        sniff(iface=INTERF, prn=_process_lldp, stop_filter=_stop_filter)
        await asyncio.sleep(5)
