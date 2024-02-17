from datatypes import Message
from scapy.all import Ether, IP, Raw

from .ethernet_entity import EthernetEntity


class IPEntity(EthernetEntity):
    def __init__(self, name: str, hw_address: str, ip_address: str) -> None:
        super().__init__(name, hw_address)
        self.ip_address = ip_address

    def _generate_base_packet(self) -> None:
        self.base_packet = Ether(src=self.hw_address) / IP(src=self.ip_address)

    def _generate_packet(self, message_details: Message):
        packet = self.base_packet.copy()
        packet[Ether].dst = message_details.hw_address
        packet[IP].dst = message_details.ip_address
        return packet / Raw(data=message_details.data)

    def _send(self, packet, times: int = 1) -> None:
        for _ in range(times):
            self.LAYER_3_SOCKET.send(packet)
