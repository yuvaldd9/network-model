from datatypes import Message
from scapy.all import Ether

from .base_entity import BaseNetworkEntity


class EthernetEntity(BaseNetworkEntity):
    def __init__(self, name: str, hw_address: str) -> None:
        super().__init__(name)
        self.hw_address = hw_address

    def _generate_base_packet(self) -> None:
        self.base_packet = Ether(src=self.hw_address)

    def _generate_packet(self, message_details: Message):
        packet = self.base_packet.copy()
        packet[Ether].dst = message_details.hw_address
        return packet

    def _send(self, packet, times: int = 1) -> None:
        for _ in range(times):
            self.LAYER_2_SOCKET.send(packet)
