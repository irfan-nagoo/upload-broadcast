from abc import ABC, abstractmethod

from apps.common.domain.message_event import MessageEvent


class MessageProducer(ABC):

    @abstractmethod
    def send_message(self, topic: str, message_event: MessageEvent):
        ...
