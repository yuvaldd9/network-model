from dataclasses import dataclass


@dataclass
class Message:
    hw_address: str
    ip_address: str
    port: int
    data: str
    times: int = 1
