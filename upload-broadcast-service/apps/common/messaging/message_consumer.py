from abc import ABC, abstractmethod


class MessageConsumer(ABC):

    @abstractmethod
    def receive_message(self, topic: str):
        ...
