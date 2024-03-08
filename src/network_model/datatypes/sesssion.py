from .messages import Message

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SessionDescriptor:
    """
    The datatype of session from model descriptor
    """

    session_name: str
    template: str
    messages: List[str]
    next_session_delay: Optional[int] = 3


@dataclass
class Session(SessionDescriptor):
    """
    The session itself
    """

    session_name: str
    messages: List[Message]
    next_session_delay: Optional[int] = 3
