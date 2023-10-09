import logging
from http import HTTPStatus

from rest_framework.response import Response

from apps.broadcast.response.artifact__search_response import ArtifactSearchResponse
from apps.common.constants.messaging_constants import PROCESSED_SUCCESS_MSG

logger = logging.getLogger(__name__)


class ArtifactSearchService:

    def __init__(self, search_artifact):
        self.search_artifact = search_artifact

    def get_artifact_search_list(self, page_no: int, page_size: int):
        logger.info("Starting get_artifact_search_list")
        artifact_list = self.search_artifact.list_artifact(page_no, page_size)
        return self.build_success_response(HTTPStatus.OK.phrase, PROCESSED_SUCCESS_MSG,
                                           artifact_list)

    def get_artifact_search_search(self, query, page_no: int, page_size: int):
        logger.info("Starting get_artifact_search_search with query[%s]", query)
        artifact_list = self.search_artifact.search_artifact(query, page_no, page_size)
        return self.build_success_response(HTTPStatus.OK.phrase, PROCESSED_SUCCESS_MSG,
                                           artifact_list)

    @staticmethod
    def build_success_response(code, message, artifact=None):
        result = [art.__dict__ for art in artifact]
        response = ArtifactSearchResponse(code, message, result)
        return Response(data=response.__dict__)
