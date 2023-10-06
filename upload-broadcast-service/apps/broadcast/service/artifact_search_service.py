import logging

logger = logging.getLogger(__name__)


class ArtifactSearchService:

    def __init__(self, search_artifact):
        self.search_artifact = search_artifact

    def get_artifact_search_list(self, page_no=0, page_size=10):
        logger.info("Starting get_artifact_search_list")
        return self.search_artifact.list_artifact(page_no, page_size)

    def get_artifact_search_search(self, query, page_no=0, page_size=10):
        logger.info("Starting get_artifact_search_search with query[%s]", query)
        return self.search_artifact.search_artifact(query, page_no, page_size)
