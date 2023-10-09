"""
URL configuration for upload_broadcast_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.broadcast.service.artifact_search_service import ArtifactSearchService
from apps.broadcast.views import ArtifactSearchAPIView
from apps.common.search.solr_search_artifact import SolrSearchArtifact
from apps.upload.models import Artifact
from apps.upload.repository.artifact_repository import ArtifactRepository
from apps.upload.service.artifact_service import ArtifactService
from apps.upload.views import ArtifactAPIView

# Upload config
artifact_repo = ArtifactRepository(Artifact.objects)
artifact_service = ArtifactService(artifact_repo)
artifact_view = ArtifactAPIView.as_view(artifact_service=artifact_service)

# Broadcast config
search_artifact = SolrSearchArtifact()
# create index if required
search_artifact.create_index()
search_service = ArtifactSearchService(search_artifact)
artifact_search_view_list = ArtifactSearchAPIView.as_view(artifact_search_service=search_service,
                                                          actions={'get': 'list'})
artifact_search_view_search = ArtifactSearchAPIView.as_view(artifact_search_service=search_service,
                                                            actions={'get': 'search'})

urlpatterns = [
    path('', artifact_view),
    path('artifact', artifact_view),
    path('artifact/<int:pk>', artifact_view),
    path('artifact-search/list', artifact_search_view_list),
    path('artifact-search/search', artifact_search_view_search),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
