from dataclasses import dataclass


@dataclass
class EntityDescriptor:
    name: str
    layer: int
    hw_address: str = ""
    ip: str = ""
    port: int = 0
