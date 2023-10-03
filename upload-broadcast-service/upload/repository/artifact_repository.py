from django.db.models import Manager


class ArtifactRepository:
    objects: Manager = None

    def __init__(self, manager):
        self.objects = manager

    def get_artifact(self, pk):
        return self.objects.get(pk=pk)

    @staticmethod
    def save_artifact(artifact):
        artifact.save()

    @staticmethod
    def update_artifact(artifact):
        artifact.save()

    @staticmethod
    def delete_artifact(artifact):
        artifact.delete()
