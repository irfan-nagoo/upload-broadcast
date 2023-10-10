import datetime

from django.utils import timezone


class ArtifactSearch:

    def __init__(self, pk: int = 0):
        self.id = pk
        self.title = ''
        self.description = ''
        self.participants = ''
        self.artifact_category = ''
        self.artifact_type = ''
        self.status = ''
        self.image = ''
        self.video = ''
        self.tags = ''
        self.published_date = datetime.date.today()
        self.modified_at = timezone.now()
        self.modified_by = ''

    @staticmethod
    def from_json(doc):
        artifact = ArtifactSearch(doc.get('id'))
        artifact.title = ArtifactSearch.get_clean_value(doc, 'title')
        artifact.description = ArtifactSearch.get_clean_value(doc, 'description')
        artifact.participants = ArtifactSearch.get_clean_value(doc, 'participants')
        artifact.artifact_category = ArtifactSearch.get_clean_value(doc, 'artifact_category')
        artifact.artifact_type = ArtifactSearch.get_clean_value(doc, 'artifact_type')
        artifact.status = ArtifactSearch.get_clean_value(doc, 'status')
        artifact.image = ArtifactSearch.get_clean_value(doc, 'image')
        artifact.video = ArtifactSearch.get_clean_value(doc, 'video')
        artifact.tags = ArtifactSearch.get_clean_value(doc, 'tags')
        artifact.published_date = ArtifactSearch.get_clean_value(doc, 'published_date')
        artifact.modified_at = ArtifactSearch.get_clean_value(doc, 'modified_at')
        artifact.modified_by = ArtifactSearch.get_clean_value(doc, 'modified_by')
        return artifact

    @staticmethod
    def get_clean_value(doc, field: str) -> str:
        return ''.join(doc.get(field, ''))
