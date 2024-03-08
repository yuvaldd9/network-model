import pytest

from network_model.datatypes import Message, EntityDescriptor
from network_model.network_entities import (
    EthernetEntity,
    IPEntity,
    TCPEntity,
    UDPEntity,
)


@pytest.fixture
def test_entity_descriptor():
    return EntityDescriptor(
        name="Test",
        protocol="Test",
        hw_address="AA:BB:CC:DD:EE:FF",
        ip="1.1.1.1",
        port=5555,
    )


@pytest.fixture
def ethernet_entity(test_entity_descriptor):
    return EthernetEntity(test_entity_descriptor)


@pytest.fixture
def ip_entity(test_entity_descriptor):
    return IPEntity(test_entity_descriptor)


@pytest.fixture
def tcp_entity(test_entity_descriptor):
    return TCPEntity(test_entity_descriptor)


@pytest.fixture
def udp_entity(test_entity_descriptor):
    return UDPEntity(test_entity_descriptor)


@pytest.fixture(scope="module")
def basic_message():
    return Message(
        sender_name="Test",
        hw_address="BB:AA:BB:AA:BB:AA",
        ip_address="0.0.0.0",
        port=8080,
        data="Basic Message",
    )
