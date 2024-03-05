import pytest

from network_model.datatypes import Message
from network_model.network_entities import (
    EthernetEntity,
    IPEntity,
    TCPEntity,
    UDPEntity,
)


@pytest.fixture
def ethernet_entity():
    return EthernetEntity("ethernet_test", "AA:BB:CC:DD:EE:FF")


@pytest.fixture
def ip_entity():
    return IPEntity("ip_test", "AA:BB:CC:DD:EE:FF", "1.1.1.1")


@pytest.fixture
def tcp_entity():
    return TCPEntity("tcp_test", "AA:BB:CC:DD:EE:FF", "1.1.1.1", 5555)


@pytest.fixture
def udp_entity():
    return UDPEntity("udp_test", "AA:BB:CC:DD:EE:FF", "1.1.1.1", 5555)


@pytest.fixture(scope="module")
def basic_message():
    return Message(
        hw_address="BB:AA:BB:AA:BB:AA",
        ip_address="0.0.0.0",
        port=8080,
        data="Basic Message",
    )
