from upload.models import Artifact as ArtifactModel


# Create your models here.

class Artifact:
    id = 0
    title = ''
    description = ''

    def to_model(self):
        artifact_model = ArtifactModel()
        artifact_model.id = self.id
        artifact_model.title = self.title
        artifact_model.description = self.description
        return artifact_model
