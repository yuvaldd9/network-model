from dataclasses import dataclass


@dataclass
class Message:
    sender_name: str
    hw_address: str
    ip_address: str
    port: int
    data: str
    times: int = 1
