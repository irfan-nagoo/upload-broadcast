import datetime

from django.utils import timezone
from rest_framework import serializers

from apps.upload.models import Artifact


class ArtifactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=500, required=True)
    participants = serializers.CharField(max_length=500, required=False)
    artifact_category = serializers.CharField(max_length=50, required=False)
    artifact_type = serializers.CharField(max_length=50, required=False)
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)
    tags = serializers.CharField(max_length=100, required=False)
    published_date = serializers.DateField(default=datetime.date.today())
    created_at = serializers.DateTimeField(default=timezone.now())
    created_by = serializers.CharField(max_length=100, default='System')
    modified_at = serializers.DateTimeField(default=timezone.now())
    modified_by = serializers.CharField(max_length=100, default='System')

    class Meta:
        model = Artifact
        fields = '__all__'
