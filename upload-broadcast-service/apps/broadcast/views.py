from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from apps.broadcast.service.artifact_search_service import ArtifactSearchService


# Create your views here.


class ArtifactSearchAPIView(GenericViewSet):
    queryset = False
    artifact_search_service: ArtifactSearchService = None

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('page_no',
                          openapi.IN_QUERY,
                          default='0',
                          type=openapi.TYPE_STRING),
        openapi.Parameter('page_size',
                          openapi.IN_QUERY,
                          default='10',
                          type=openapi.TYPE_STRING)]
    )
    @action(methods=['GET'], detail=False)
    def list(self, request):
        page_no = request.GET.get('page_no', '0')
        page_size = request.GET.get('page_size', '10')
        return self.artifact_search_service.get_artifact_search_list(int(page_no), int(page_size))

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('query',
                          openapi.IN_QUERY,
                          required=True,
                          type=openapi.TYPE_STRING),
        openapi.Parameter('page_no',
                          openapi.IN_QUERY,
                          default='0',
                          type=openapi.TYPE_STRING),
        openapi.Parameter('page_size',
                          openapi.IN_QUERY,
                          default='10',
                          type=openapi.TYPE_STRING)]
    )
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.GET.get('query')
        page_no = request.GET.get('page_no', '0')
        page_size = request.GET.get('page_size', '10')
        return self.artifact_search_service.get_artifact_search_search(query, int(page_no), int(page_size))
