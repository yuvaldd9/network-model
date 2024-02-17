import os
import pytest

from network_model.loader import Loader


def test_loader_sanity():
    loader = Loader(
        os.path.realpath("tests/loader/test_model_descriptors/sanity_network_model.yml")
    )
    assert loader


def test_not_exist_model_descriptor():
    with pytest.raises(ValueError) as file_error:
        Loader("not_exist_model_descriptor.yml")
    assert (
        str(file_error.value)
        == "Model descriptor file not_exist_model_descriptor.yml does not exists"
    )


def test_not_valid_model():
    with pytest.raises(ValueError) as file_error:
        loader = Loader(
            os.path.realpath(
                "tests/loader/test_model_descriptors/bad_network_model.yml"
            )
        )
        loader.load()
    assert str(file_error.value) == "Bad model file"
