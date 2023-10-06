from enum import Enum


class ArtifactType(Enum):
    TECHNOLOGY = 'Technology'
    SCIENCE = 'Science'
    ENGINEERING = 'Engineering'
    NATURE = 'Nature'

    @classmethod
    def choices(cls):
        return tuple((artifact_type.name, artifact_type.value) for artifact_type in cls)

    @classmethod
    def __contains__(cls, value):
        values = [status.value for status in ArtifactType]
        return values.__contains__(value)
