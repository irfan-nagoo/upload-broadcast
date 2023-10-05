from rest_framework.views import APIView

from apps.upload.service.artifact_service import ArtifactService


# Create your views here.

class ArtifactAPIView(APIView):
    artifact_service: ArtifactService = None

    def __int__(self, artifact_service):
        self.artifact_service = artifact_service

    def post(self, request):
        return self.artifact_service.save_artifact(request.data)

    def get(self, request, pk=1):
        return self.artifact_service.get_artifact(pk)

    def put(self, request, pk):
        return self.artifact_service.update_artifact(request.data, pk)

    def delete(self, request, pk):
        return self.artifact_service.delete_artifact(pk)
