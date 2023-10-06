import datetime

from django.db import models
from django.utils import timezone

from apps.common.constants.artifact_type import ArtifactType
from apps.common.constants.category_type import CategoryType
from apps.common.constants.status_type import StatusType
from apps.common.util.common_util import get_image_uri, get_video_uri


# Create your models here.

class Artifact(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    participants = models.CharField(max_length=500, blank=True)
    artifact_category = models.CharField(max_length=50, blank=True,
                                         choices=CategoryType.choices())
    artifact_type = models.CharField(max_length=50, blank=True,
                                     choices=ArtifactType.choices())
    status = models.CharField(max_length=20, default=StatusType.ACTIVE.value,
                              choices=StatusType.choices())
    image = models.ImageField(upload_to=get_image_uri, default='artifact/images/no-image.jpg',
                              db_column='image_url')
    video = models.FileField(upload_to=get_video_uri, default='artifact/videos/no-video.mp4',
                             db_column='video_url')
    tags = models.CharField(max_length=100, blank=True)
    published_date = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=100, default='System')
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, default='System')

    objects = models.Manager()

    class Meta:
        db_table = 'md_artifact'
