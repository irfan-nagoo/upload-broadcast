from django.db import models


# Create your models here.

class Artifact(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    objects = models.Manager()
