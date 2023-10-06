import datetime

from django.utils import timezone


class ArtifactSearch:

    def __init__(self, pk=0):
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
