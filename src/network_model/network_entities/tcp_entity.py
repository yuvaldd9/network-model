from datatypes import Message
from scapy.all import Ether, IP, TCP, Raw

from .ip_entity import IPEntity


class TCPEntity(IPEntity):
    def __init__(self, name: str, hw_address: str, ip_address: str, port: int) -> None:
        super().__init__(name, hw_address, ip_address)
        self.port = port

    def _generate_base_packet(self) -> None:
        self.base_packet = (
            Ether(src=self.hw_address) / IP(src=self.ip_address) / TCP(sport=self.port)
        )

    def _generate_packet(self, message_details: Message):
        packet = self.base_packet.copy()
        packet[Ether].dst = message_details.hw_address
        packet[IP].dst = message_details.ip_address
        packet[TCP].dport = message_details.port
        return packet / Raw(data=message_details.data)
