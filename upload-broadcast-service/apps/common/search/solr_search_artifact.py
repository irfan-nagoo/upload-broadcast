import json
import logging
from http import HTTPMethod

from django.conf import settings
from urllib3 import *

from apps.common.constants.solr_admin_action_type import SolrAdminActionType
from apps.common.domain.artifact_search import ArtifactSearch
from apps.common.search.search_artifact import SearchArtifact

logger = logging.getLogger(__name__)


class SolrSearchArtifact(SearchArtifact):

    def add_artifact(self, artifact: ArtifactSearch):
        response = self.update_artifact_doc(artifact)
        logger.info("Document add status: %d", response.status)

    def update_artifact(self, artifact: ArtifactSearch):
        response = self.update_artifact_doc(artifact)
        logger.info("Document update status: %d", response.status)

    def delete_artifact(self, artifact: ArtifactSearch):
        # soft delete only
        response = self.update_artifact_doc(artifact)
        logger.info("Document delete status: %d", response.status)

    def list_artifact(self, page_no: int = 0, page_size: int = 10):
        start = page_no * page_size
        response = request(HTTPMethod.GET,
                           settings.SOLR_BASE_V2_URL + '/' + settings.SOLR_CORE + '/select'
                           + '?q=*:*'
                           + '&start=' + start.__str__()
                           + '&rows=' + page_size.__str__()
                           + '&wt=json')

        logger.info("Number of documents found: %d", response.json()['response']['numFound'])
        result = []
        for doc in response.json()['response']['docs']:
            result.append(ArtifactSearch.from_json(doc))
        return result

    def search_artifact(self, query: str, page_no: int = 0, page_size: int = 10):
        start = page_no * page_size
        response = request(HTTPMethod.GET,
                           settings.SOLR_BASE_V2_URL + '/' + settings.SOLR_CORE + '/select'
                           + '?q=title:*' + query + '* description:*' + query + '*'
                           + '&start=' + start.__str__()
                           + '&rows=' + page_size.__str__()
                           + '&wt=json')

        logger.info("Number of documents found: %d", response.json()['response']['numFound'])
        result = []
        for doc in response.json()['response']['docs']:
            result.append(ArtifactSearch.from_json(doc))
        return result

    def create_index(self):
        status_response = self.get_solr_admin_response_v2(HTTPMethod.GET, SolrAdminActionType.STATUS,
                                                          settings.SOLR_CORE)
        if len(status_response.json()['status'][settings.SOLR_CORE]) == 0:
            logger.info("Start creating core[%s]", settings.SOLR_CORE)
            response = self.get_solr_admin_response_v2(HTTPMethod.POST, SolrAdminActionType.CREATE,
                                                       settings.SOLR_CORE, '_default')
            if response.json()['core'] == settings.SOLR_CORE:
                logger.info('Core created Successfully!')
        else:
            logger.info("Core already exists")

    def delete_index(self):
        response = self.get_solr_admin_response_v2(HTTPMethod.POST, SolrAdminActionType.UNLOAD,
                                                   settings.SOLR_CORE)
        if response.status == 200:
            logger.info('Core deleted successfully!')

    @staticmethod
    def get_solr_admin_response_v2(method: HTTPMethod,
                                   action: SolrAdminActionType,
                                   core: str,
                                   configset: str | None = None):
        match action:
            case SolrAdminActionType.STATUS:
                return request(method, settings.SOLR_BASE_V2_URL + '/' + core)
            case SolrAdminActionType.UNLOAD:
                return request(method, settings.SOLR_BASE_V2_URL + '/' + core, json={action: {}})
            case SolrAdminActionType.CREATE:
                return request(method, settings.SOLR_BASE_V2_URL, json={action: {
                    'name': core,
                    'configSet': configset}
                })
            case _:
                return 'Invalid action type'

    @staticmethod
    def update_artifact_doc(artifact: ArtifactSearch):
        return request(HTTPMethod.POST,
                       settings.SOLR_BASE_V2_URL + '/' + settings.SOLR_CORE + '/update/json'
                       + '?f=/**'
                       + '&softCommit=true',
                       body=json.dumps(artifact, default=str),
                       headers={'Content-type': 'application/json'})
