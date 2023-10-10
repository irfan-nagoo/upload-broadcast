import json
import logging

from confluent_kafka import Producer
from django.conf import settings

from apps.common.domain.message_event import MessageEvent
from apps.common.messaging.message_producer import MessageProducer

logger = logging.getLogger(__name__)


class KafkaMessageProducer(MessageProducer):

    def __init__(self):
        self.kafka_client = Producer({'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVER})

    def send_message(self, topic: str, message_event: MessageEvent):
        # trigger any previous delivery report callback
        self.kafka_client.poll(0)
        self.kafka_client.produce(topic, json.dumps(message_event.__dict__), callback=self.send_confirmation)
        # waiting for delivery
        self.kafka_client.flush()

    @staticmethod
    def send_confirmation(err, msg):
        if err is not None:
            logger.error('Error occurred while delivering message: %s', err)
        else:
            logger.info('Message successfully delivered to topic[%s]', msg.topic())
