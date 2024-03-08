import os
import pytest

from network_model.handlers import ModelHandler
from network_model.datatypes import Message, Session, EntityDescriptor
from network_model.network_entities import TCPEntity, UDPEntity


@pytest.fixture
def valid_model_descriptor_path():
    return os.path.realpath(
        "tests/loader/test_model_descriptors/sanity_network_model.yml"
    )


@pytest.fixture
def not_valid_model_descriptor_path():
    return os.path.realpath(
        "tests/loader/test_model_descriptors/sanity_network_model.yml"
    )


def additional_valid_model_descriptor_path():
    return os.path.realpath(
        "tests/loader/test_model_descriptors/sanity_network_model.yml"
    )


@pytest.fixture
def model_entities_1():
    return {
        "Alice": TCPEntity(
            EntityDescriptor(
                name="Alice", protocol="tcp", hw_address="", ip="10.0.0.1", port=8080
            )
        ),
        "Bob": UDPEntity(
            EntityDescriptor(
                name="Bob", protocol="udp", hw_address="", ip="10.0.0.2", port=8081
            )
        ),
    }


@pytest.fixture
def model_sessions_1():
    return [
        Session(
            session_name="example1",
            template="custom",
            messages=[
                Message(
                    sender_name="Alice",
                    hw_address="",
                    ip_address="10.0.0.2",
                    port=8081,
                    data="Hello",
                ),
                Message(
                    sender_name="Bob",
                    hw_address="",
                    ip_address="10.0.0.1",
                    port=8080,
                    data="Hi",
                ),
            ],
        )
    ]


@pytest.fixture
def model_handler_1(model_entities_1, model_sessions_1):
    return ModelHandler(model_entities_1, model_sessions_1)
