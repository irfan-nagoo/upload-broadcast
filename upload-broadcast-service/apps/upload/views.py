from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from apps.upload.serializers import ArtifactSerializer
from apps.upload.service.artifact_service import ArtifactService


# Create your views here.

class ArtifactAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    artifact_service: ArtifactService = None

    def get(self, request, pk=1):
        return self.artifact_service.get_artifact(pk)

    @swagger_auto_schema(request_body=ArtifactSerializer,
                         manual_parameters=[
                             openapi.Parameter('id',
                                               openapi.IN_PATH,
                                               type=openapi.TYPE_STRING)]
                         )
    def put(self, request, pk):
        return self.artifact_service.update_artifact(request.data, pk)

    def delete(self, request, pk):
        return self.artifact_service.delete_artifact(pk)


class ArtifactPostAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    artifact_service: ArtifactService = None

    @swagger_auto_schema(request_body=ArtifactSerializer)
    def post(self, request):
        return self.artifact_service.save_artifact(request.data)
