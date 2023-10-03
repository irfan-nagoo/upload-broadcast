from rest_framework.response import Response

from upload.repository.artifact_repository import ArtifactRepository
from upload.serializers import ArtifactSerializer


class ArtifactService:
    artifact_repo: ArtifactRepository = None

    def __init__(self, artifact_repo):
        self.artifact_repo = artifact_repo

    def get_artifact(self, pk):
        artifact = self.artifact_repo.get_artifact(pk)
        serializer = ArtifactSerializer(artifact)
        return Response({"code": "OK",
                         "message": "Request processed successfully",
                         "artifact": serializer.data})

    def save_artifact(self, data):
        serializer = ArtifactSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.artifact_repo.save_artifact(serializer)
        return Response({"code": "OK",
                         "message": "Request processed successfully",
                         "artifact": serializer.data})

    def update_artifact(self, data, pk):
        artifact = self.artifact_repo.get_artifact(pk)
        serializer = ArtifactSerializer(artifact, data=data)
        serializer.is_valid(raise_exception=True)
        self.artifact_repo.update_artifact(serializer)
        return Response({"code": "OK",
                         "message": "Request processed successfully",
                         "artifact": serializer.data})

    def delete_artifact(self, pk):
        artifact = self.artifact_repo.get_artifact(pk)
        self.artifact_repo.delete_artifact(artifact)
        return Response({"code": "OK",
                         "message": "Request processed successfully", })
