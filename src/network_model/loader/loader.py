import re
import os
import dataconf

from typing import List, Dict, Optional

from ..handlers import ModelHandler
from ..datatypes import ModelDescriptor, Session, Message
from ..network_entities import (
    BaseNetworkEntity,
    EthernetEntity,
    IPEntity,
    TCPEntity,
    UDPEntity,
)

# Error messages
BAD_MESSAGE_DESCRIPTION = (
    "Message are not described accroding to the format Sender->Receiver | Data"
)
NOT_EXISTS_ENTITIES = "Your message description contains not defined network entities"

# Parsing Consts
MESSAGE_PATTERN_REGEX = r"^(.*?)->(.*?) \| (.*)$"
ENTITIES_BY_PROTOCOL: Dict[str, BaseNetworkEntity] = {
    "ether": EthernetEntity,
    "ip": IPEntity,
    "tcp": TCPEntity,
    "udp": UDPEntity,
}


class Loader:
    def __init__(self, descriptor_file: str) -> None:
        self._check_descriptor(descriptor_file)
        self.descriptor_file: str = descriptor_file

    def _check_descriptor(self, descriptor_path: str) -> bool:
        """
        Validate the input descriptor file
        Return True if file is valid, else Raise Value Error
        """

        if not os.path.exists(descriptor_path):
            raise ValueError(f"Model descriptor file {descriptor_path} does not exists")

        return True

    def load(self, new_descriptor: Optional[str] = None) -> ModelHandler:
        model_descriptor = self._load(
            new_descriptor
            if new_descriptor and self._check_descriptor(new_descriptor)
            else self.descriptor_file
        )

        return self._parse_model(model_descriptor)

    def _parse_model(self, model_descriptor: ModelDescriptor) -> ModelHandler:
        """Parse the ModelDescriptor to ModelHandler"""

        # Entities
        model_entities = {
            entity.name: ENTITIES_BY_PROTOCOL[entity.protocol](entity)
            for entity in model_descriptor.entities
        }

        # Sessions
        model_sessions: List[Session] = []
        for session in model_descriptor.sessions:
            model_sessions.append(
                Session(
                    session.session_name,
                    session.template,
                    self._parse_messages(model_entities, session.messages),
                    session.next_session_delay,
                )
            )

        return ModelHandler(model_entities, model_sessions)

    def _parse_messages(
        self, entities: Dict[str, BaseNetworkEntity], message_descriptions: List[str]
    ) -> List[Message]:
        messages: List[Message] = []

        for message in message_descriptions:
            match = re.match(MESSAGE_PATTERN_REGEX, message)
            if match:
                sender, receiver, data = match.group(1), match.group(2), match.group(3)

                # Check if sender and receiver are defined in the model entities
                if not set([sender, receiver]) <= set(entities.keys()):
                    raise ValueError(NOT_EXISTS_ENTITIES)

                messages.append(
                    Message(
                        sender_name=sender,
                        hw_address=entities[receiver].hw_address,
                        ip_address=entities[receiver].ip_address,
                        port=entities[receiver].port,
                        data=data,
                    )
                )
            else:
                raise ValueError(BAD_MESSAGE_DESCRIPTION)

        return messages

    def _load(self, descriptor_file: str) -> ModelDescriptor:
        return dataconf.file(descriptor_file, ModelDescriptor)
