import os
import dataconf

from typing import Optional
from ..datatypes import ModelDescriptor


class Loader:
    def __init__(self, descriptor_file: str):
        self._check_descriptor(descriptor_file)

        self.descriptor_file: str = descriptor_file

    def _check_descriptor(self, descriptor_path: str) -> bool:
        """
        Validate the input descriptor file
        Return True if file is valid, else Raise Value Error
        """

        if not os.path.isfile(descriptor_path):
            raise ValueError(f"Model descriptor file {descriptor_path} does not exists")

        return True

    def load(self, new_descriptor: Optional[str] = None) -> ModelDescriptor:
        return self._load(
            new_descriptor
            if new_descriptor and self._check_descriptor(new_descriptor)
            else self.descriptor_file
        )

    def _load(self, descriptor_file: str) -> ModelDescriptor:
        try:
            return dataconf.file(descriptor_file, ModelDescriptor)
        except Exception as e:
            raise ValueError(e)
