from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SessionDescriptor:
    """
    The datatype of session from model descriptor
    """

    session_name: str
    interface: str
    template: str
    entities: List[str]
    messages: List[str]
    next_session_delay: Optional[int] = 10
