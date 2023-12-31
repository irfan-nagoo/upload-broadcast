import logging
from http import HTTPStatus

from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from apps.common.constants.action_type import ActionType
from apps.common.constants.messaging_constants import PROCESSED_SUCCESS_MSG, VALIDATION_FAILED_MSG
from apps.common.constants.status_type import StatusType
from apps.common.domain.message_event import MessageEvent
from apps.common.messaging.message_producer import MessageProducer
from apps.upload.repository.artifact_repository import ArtifactRepository
from apps.upload.response.artifact_response import ArtifactResponse
from apps.upload.serializers import ArtifactSerializer

logger = logging.getLogger(__name__)


class ArtifactService:
    artifact_repo: ArtifactRepository = None

    def __init__(self, artifact_repo: ArtifactRepository, message_producer: MessageProducer):
        self.artifact_repo = artifact_repo
        self.message_producer = message_producer

    def get_artifact(self, pk):
        logger.info("Starting get_artifact with id[%d]", pk)
        artifact = self.artifact_repo.get_artifact(pk)
        serializer = ArtifactSerializer(artifact)
        return self.build_success_response(HTTPStatus.OK.phrase, PROCESSED_SUCCESS_MSG,
                                           serializer.data)

    def save_artifact(self, data):
        logger.info("Starting save_artifact")
        serializer = ArtifactSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            self.artifact_repo.save_artifact(serializer)
            # send message for search indexing
            self.message_producer.send_message(settings.KAFKA_TOPIC,
                                               MessageEvent(ActionType.CREATE.name, serializer.data))
            return self.build_success_response(HTTPStatus.OK.phrase, PROCESSED_SUCCESS_MSG,
                                               serializer.data)
        else:
            raise ValidationError(VALIDATION_FAILED_MSG, HTTPStatus.BAD_REQUEST.phrase)

    def update_artifact(self, data, pk):
        logger.info("Starting update_artifact with id[%d]", pk)
        artifact = self.artifact_repo.get_artifact(pk)
        serializer = ArtifactSerializer(artifact, data=data)
        if serializer.is_valid(raise_exception=True):
            self.artifact_repo.update_artifact(serializer)
            # send message for search indexing
            self.message_producer.send_message(settings.KAFKA_TOPIC,
                                               MessageEvent(ActionType.UPDATE.name, serializer.data))
            return self.build_success_response(HTTPStatus.OK.phrase, PROCESSED_SUCCESS_MSG,
                                               serializer.data)
        else:
            raise ValidationError(VALIDATION_FAILED_MSG, HTTPStatus.BAD_REQUEST.phrase)

    def delete_artifact(self, pk):
        logger.info("Starting delete_artifact with id[%d]", pk)
        artifact = self.artifact_repo.get_artifact(pk)
        artifact.status = StatusType.DELETED.value
        # soft delete only
        self.artifact_repo.update_artifact(artifact)
        # send message for search indexing
        self.message_producer.send_message(settings.KAFKA_TOPIC,
                                           MessageEvent(ActionType.DELETE.name, ArtifactSerializer(artifact).data))
        return self.build_success_response(HTTPStatus.OK.phrase, PROCESSED_SUCCESS_MSG)

    @staticmethod
    def build_success_response(code, message, artifact=None):
        response = ArtifactResponse(code, message, artifact)
        return Response(data=response.__dict__)
