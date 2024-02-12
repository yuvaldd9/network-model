import tomli

from pathlib import Path


# TODO: Finish the validation of the conf file
# and then convert the file to Datatypes of
# Model -> Entities, Sessions
 
class Config:
    def __init__(self, config_file: Path):
        self.config_file: Path = config_file

    def _validate(self):
        pass
