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
        artifact.title = doc.get('title')
        artifact.description = doc.get('description')
        artifact.participants = doc.get('participants')
        artifact.artifact_category = doc.get('artifact_category')
        artifact.artifact_type = doc.get('artifact_type')
        artifact.status = doc.get('status')
        artifact.image = doc.get('image')
        artifact.video = doc.get('video')
        artifact.tags = doc.get('tags')
        artifact.published_date = doc.get('published_date')
        artifact.modified_at = doc.get('modified_at')
        artifact.modified_by = doc.get('modified_by')
        return artifact
