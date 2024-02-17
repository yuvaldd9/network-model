from dataclasses import dataclass


@dataclass
class Message:
    sender_name: str
    receiver_name: str
    data: str
    times: int = 1
