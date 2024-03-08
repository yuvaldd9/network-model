import time

from typing import List, Dict

from ..datatypes import Session
from ..network_entities import BaseNetworkEntity


MESSAGE_DELAY = 0.5


class ModelHandler:
    def __init__(self, entities: Dict[str, BaseNetworkEntity], sessions: List[Session]):
        self.entities: Dict[str, BaseNetworkEntity] = entities
        self.sessions: List[Session] = sessions

    def model(self):
        for session in self.sessions:
            self._play_session(session)

    def _play_session(self, session: Session):
        for message in session.messages:
            self.entities[message.sender_name].send(message)
            time.sleep(MESSAGE_DELAY)

        time.sleep(session.next_session_delay)
