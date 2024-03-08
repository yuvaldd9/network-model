from dataclasses import dataclass


@dataclass
class EntityDescriptor:
    name: str
    protocol: str
    hw_address: str = ""
    ip: str = ""
    port: int = 0
