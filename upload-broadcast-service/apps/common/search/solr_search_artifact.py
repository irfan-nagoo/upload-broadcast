import pysolr
from django.conf import settings

from apps.common.search.search_artifact import SearchArtifact


class SolrSearchArtifact(SearchArtifact):

    def add_artifact(self, artifact):
        self.get_solr_client().add(artifact)

    def update_artifact(self, artifact):
        self.get_solr_client().add(artifact, fieldUpdates={
            'title': 'set'
        })

    def delete_artifact(self, artifact):
        self.get_solr_client().add(artifact, fieldUpdates={
            'status': 'set'
        })

    def list_artifact(self, page_no=0, page_size=10):
        result = self.get_solr_client().search("*:*")

    def search_artifact(self, query, page_no=0, page_size=10):
        result = self.get_solr_client().search("*:" + query)

    def create_index(self):
        solr_admin = self.get_solr_admin_client()
        result = solr_admin.status(settings.SOLR_CORE)

    def delete_index(self):
        self.get_solr_admin_client().unload(settings.SOLR_CORE)

    @staticmethod
    def get_solr_client():
        return pysolr.Solr(settings.SOLR_BASE_URL + settings.SOLR_CORE, always_commit=True)

    @staticmethod
    def get_solr_admin_client():
        return pysolr.SolrCoreAdmin(settings.SOLR_BASE_URL + '/admin/cores')
