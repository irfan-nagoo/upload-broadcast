from apps.common.domain.artifact_search import ArtifactSearch


def artifact_to_artifact_search(artifact):
    artifact_search = ArtifactSearch(artifact.id)
    artifact_search.title = artifact.title
    artifact_search.description = artifact.description
    artifact_search.participants = artifact.participants
    artifact_search.artifact_category = artifact.artifact_category
    artifact_search.artifact_type = artifact.artifact_type
    artifact_search.status = artifact.status
    artifact_search.image = artifact.image.url
    artifact_search.video = artifact.video.url
    artifact_search.tags = artifact.tags
    artifact_search.published_date = artifact.published_date
    artifact_search.modified_at = artifact.modified_at
    artifact_search.modified_by = artifact.modified_by
    return artifact_search
