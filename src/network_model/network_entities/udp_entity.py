from scapy.all import Ether, IP, UDP

from ..datatypes import Message
from .ip_entity import IPEntity


class UDPEntity(IPEntity):
    def __init__(self, name: str, hw_address: str, ip_address: str, port: int) -> None:
        super().__init__(name, hw_address, ip_address)
        self.port = port

    def _generate_base_packet(self) -> None:
        self._base_packet = (
            Ether(src=self.hw_address) / IP(src=self.ip_address) / UDP(sport=self.port)
        )

    def _generate_packet(self, message_details: Message):
        packet = self._base_packet.copy()
        packet[Ether].dst = message_details.hw_address
        packet[IP].dst = message_details.ip_address
        packet[UDP].dport = message_details.port
        return packet
