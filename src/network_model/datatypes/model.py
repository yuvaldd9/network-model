from .entity import EntityDescriptor
from .sesssion import SessionDescriptor

from typing import List
from dataclasses import dataclass


@dataclass
class ModelDescriptor:
    name: str
    entities: List[EntityDescriptor]
    sessions: List[SessionDescriptor]
