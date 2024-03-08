from scapy.all import Ether

from network_model.datatypes.entity import EntityDescriptor

from ..datatypes import Message
from .base_entity import BaseNetworkEntity


class EthernetEntity(BaseNetworkEntity):
    def __init__(self, entity_descriptor: EntityDescriptor) -> None:
        super().__init__(entity_descriptor)

    def _generate_base_packet(self) -> None:
        self._base_packet = Ether(src=self.hw_address)

    def _generate_packet(self, message_details: Message):
        packet = self._base_packet.copy()
        packet[Ether].dst = message_details.hw_address
        return packet

    def _send(self, packet, times: int = 1) -> None:
        for _ in range(times):
            self.LAYER_2_SOCKET.send(packet)
