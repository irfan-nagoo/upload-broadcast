from rest_framework import serializers

from apps.upload.models import Artifact


class ArtifactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=10, required=True)
    description = serializers.CharField(max_length=500, required=True)

    class Meta:
        model = Artifact
        fields = ['id', 'title', 'description']
