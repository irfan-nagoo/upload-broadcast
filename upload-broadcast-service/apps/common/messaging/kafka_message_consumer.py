import json
import logging

from confluent_kafka import Consumer
from django.conf import settings

from apps.common.constants.action_type import ActionType
from apps.common.messaging.message_consumer import MessageConsumer
from apps.common.search.search_artifact import SearchArtifact

logger = logging.getLogger(__name__)


class KafkaMessageConsumer(MessageConsumer):

    def __init__(self, search_artifact: SearchArtifact):
        self.search_artifact = search_artifact
        self.kafka_consumer = Consumer({
            'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVER,
            'group.id': settings.KAFKA_GROUP,
            'auto.offset.reset': settings.KAFKA_OFFSET_RESET
        })

    def receive_message(self, topic: str):
        # subscribe to topic
        logger.info('Subscribing to Kafka topic')
        self.kafka_consumer.subscribe([topic])

        while True:
            message = self.kafka_consumer.poll(1.0)
            if message is None:
                continue
            elif message.error():
                logger.error('Kafka Consumer error occurred: %s', message.error())
                continue

            logger.info("Message Received: %s", message.value().decode('utf-8'))
            message_event = json.loads(message.value().decode('utf-8'))
            action = message_event.get('action')
            match ActionType[action]:
                case ActionType.CREATE:
                    self.search_artifact.add_artifact(message_event.get('artifact'))
                case ActionType.UPDATE:
                    self.search_artifact.update_artifact(message_event.get('artifact'))
                case ActionType.DELETE:
                    self.search_artifact.add_artifact(message_event.get('artifact'))
                case _:
                    logger.info('Invalid action[%s]', action)

        self.kafka_consumer.close()
