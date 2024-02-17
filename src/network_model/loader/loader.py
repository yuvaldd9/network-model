import os
import dataconf

from ..datatypes import ModelDescriptor


class Loader:
    def __init__(self, config_file: str):
        if not os.path.isfile(config_file):
            raise ValueError(f"Model descriptor file {config_file} does not exists")
        self.config_file: str = config_file

    def load(self) -> ModelDescriptor:
        try:
            return dataconf.file(self.config_file, ModelDescriptor)
        except:
            # TODO: Better error messafe
            raise ValueError("Bad model file")
