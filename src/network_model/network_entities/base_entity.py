from scapy.all import Raw, conf
from abc import ABC, abstractmethod

from ..datatypes import Message


class BaseNetworkEntity(ABC):
    LAYER_2_SOCKET = conf.L2socket()
    LAYER_3_SOCKET = conf.L3socket()

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name: str = name
        self._base_packet = None

    @abstractmethod
    def _generate_base_packet(self) -> None:
        """
        Generate according to the network entity, its
        base packet which will be sent each send
        """
        pass

    @abstractmethod
    def _generate_packet(self, message_details: Message):
        """
        Generates the packet according to the

        :param message_details: _description_
        :type message_details: Message
        """
        pass

    @abstractmethod
    def _send(self, packet, int: int = 1) -> None:
        """
        The actual sending of the packet, differs from
        each entity due to its socket

        :param packet: The generated packet from self.send()
        :type packet: _type_
        """
        pass

    def send(self, message_details: Message) -> None:
        """
        Generates the packet and then sends it

        :param message_details: Dataclass of the message details
        :type message_details: Message
        """

        if not self._base_packet:
            self._generate_base_packet()

        packet_to_send = self._generate_packet(message_details) / Raw(
            load=message_details.data
        )
        self._send(packet_to_send, message_details.times)
