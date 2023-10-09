from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from apps.broadcast.service.artifact_search_service import ArtifactSearchService


# Create your views here.


class ArtifactSearchAPIView(GenericViewSet):
    queryset = False
    artifact_search_service: ArtifactSearchService = None

    def __int__(self, artifact_search_service):
        self.artifact_search_service = artifact_search_service

    @action(methods=['GET'], detail=False)
    def list(self, request):
        page_no = request.GET.get('page_no', '0')
        page_size = request.GET.get('page_size', '10')
        return self.artifact_search_service.get_artifact_search_list(int(page_no), int(page_size))

    @action(methods='GET', detail=False)
    def search(self, request):
        query = request.GET.get('query')
        page_no = request.GET.get('page_no', '0')
        page_size = request.GET.get('page_size', '10')
        return self.artifact_search_service.get_artifact_search_search(query, int(page_no), int(page_size))
