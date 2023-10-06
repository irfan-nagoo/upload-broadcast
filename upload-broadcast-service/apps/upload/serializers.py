from http import HTTPStatus

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.common.constants.artifact_type import ArtifactType
from apps.common.constants.category_type import CategoryType
from apps.common.constants.messaging_constants import INVALID_VALUE_MSG
from apps.common.constants.status_type import StatusType
from apps.upload.models import Artifact


class ArtifactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=500, required=True)
    participants = serializers.CharField(max_length=500, required=False)
    artifact_category = serializers.CharField(max_length=50, required=False)
    artifact_type = serializers.CharField(max_length=50, required=False)
    status = serializers.CharField(max_length=20, required=False)
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    tags = serializers.CharField(max_length=100, required=False)
    published_date = serializers.DateField(required=False)
    created_at = serializers.DateTimeField(required=False)
    created_by = serializers.CharField(max_length=100, required=False)
    modified_at = serializers.DateTimeField(required=False)
    modified_by = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Artifact
        fields = '__all__'

    @staticmethod
    def validate_status(value):
        if not StatusType.__contains__(value):
            raise ValidationError(INVALID_VALUE_MSG % value, HTTPStatus.BAD_REQUEST.phrase)
        return value

    @staticmethod
    def validate_artifact_category(value):
        if not CategoryType.__contains__(value):
            raise ValidationError(INVALID_VALUE_MSG % value, HTTPStatus.BAD_REQUEST.phrase)
        return value

    @staticmethod
    def validate_artifact_type(value):
        if not ArtifactType.__contains__(value):
            raise ValidationError(INVALID_VALUE_MSG % value, HTTPStatus.BAD_REQUEST.phrase)
        return value
