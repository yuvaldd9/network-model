import pytest

from network_model.loader import Loader


def test_loader_sanity(valid_model_descriptor_path):
    assert Loader(valid_model_descriptor_path)


def test_not_exist_model_descriptor():
    with pytest.raises(ValueError) as file_error:
        Loader("not_exist_model_descriptor.yml")
    assert (
        str(file_error.value)
        == "Model descriptor file not_exist_model_descriptor.yml does not exists"
    )


def test_load(valid_model_descriptor_path, model_handler_1):
    loader = Loader(valid_model_descriptor_path)
    test_model = loader.load()
    assert test_model.sessions == model_handler_1.sessions
    assert test_model.entities == model_handler_1.entities


def test_not_valid_message_pattern(valid_model_descriptor_path):
    loader = Loader(valid_model_descriptor_path)
    with pytest.raises(ValueError) as message_error:
        loader._parse_messages({}, ["bad message description"])
        assert (
            str(message_error)
            == "Message are not described accroding to the format Sender->Receiver | Data"
        )


def test_not_valid_message_entities(not_valid_messages_model_descriptor_path):
    loader = Loader(not_valid_messages_model_descriptor_path)
    with pytest.raises(ValueError) as message_error:
        loader.load()
        assert (
            str(message_error)
            == "Your message description contains not defined network entities"
        )


def test_additional_model(
    model_handler_2, valid_model_descriptor_path, additional_valid_model_descriptor_path
):
    loader = Loader(valid_model_descriptor_path)
    addtional_model = loader.load(new_descriptor=additional_valid_model_descriptor_path)
    assert addtional_model.sessions == model_handler_2.sessions
    assert addtional_model.entities == model_handler_2.entities
