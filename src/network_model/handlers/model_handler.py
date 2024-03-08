import time

from typing import List, Dict

from ..datatypes import Session
from ..network_entities import BaseNetworkEntity


MESSAGE_DELAY = 0.01


class ModelHandler:
    def __init__(self, entities: Dict[str, BaseNetworkEntity], sessions: List[Session]):
        self.entities: Dict[str, BaseNetworkEntity] = entities
        self.sessions: List[Session] = sessions

    def play(self):
        for session in self.sessions[:-1]:
            self._play_session(session)
            time.sleep(session.next_session_delay)

        # The last session should not "delay" the model
        self._play_session(self.sessions[-1])

    def _play_session(self, session: Session):
        for message in session.messages:
            self.entities[message.sender_name].send(message)
            time.sleep(MESSAGE_DELAY)
