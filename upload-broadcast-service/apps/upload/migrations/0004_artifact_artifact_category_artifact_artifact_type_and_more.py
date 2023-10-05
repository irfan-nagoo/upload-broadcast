# Generated by Django 4.2.5 on 2023-10-05 14:46

import apps.common.util.common_util
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_artifact_video_alter_artifact_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='artifact_category',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='artifact',
            name='artifact_type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='artifact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 5, 14, 45, 27, 287091, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='artifact',
            name='created_by',
            field=models.CharField(default='System', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artifact',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 5, 14, 45, 27, 287091, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='artifact',
            name='modified_by',
            field=models.CharField(default='System', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artifact',
            name='participants',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='artifact',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 5, 14, 45, 27, 287091, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='artifact',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='image',
            field=models.ImageField(blank=True, db_column='image_url', default='artifact/images/no-image.jpg', upload_to=apps.common.util.common_util.get_image_uri),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='video',
            field=models.FileField(blank=True, db_column='video_url', default='artifact/videos/no-video.mp4', upload_to=apps.common.util.common_util.get_video_uri),
        ),
    ]
