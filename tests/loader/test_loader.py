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
