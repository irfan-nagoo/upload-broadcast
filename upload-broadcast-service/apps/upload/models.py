import datetime

from django.db import models
from django.utils import timezone

from apps.common.util.common_util import get_image_uri, get_video_uri


# Create your models here.

class Artifact(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    participants = models.CharField(max_length=500, blank=True)
    artifact_category = models.CharField(max_length=50, blank=True)
    artifact_type = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to=get_image_uri,
                              default='artifact/images/no-image.jpg', db_column='image_url')
    video = models.FileField(blank=True, upload_to=get_video_uri,
                             default='artifact/videos/no-video.mp4', db_column='video_url')
    tags = models.CharField(max_length=100, blank=True)
    published_date = models.DateField(default=datetime.date.today())
    created_at = models.DateTimeField(default=timezone.now())
    created_by = models.CharField(max_length=100)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100)

    objects = models.Manager()
