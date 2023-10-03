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
from django.contrib import admin
from django.urls import path, include

from upload import views
from upload.models import Artifact
from upload.repository.artifact_repository import ArtifactRepository
from upload.service.artifact_service import ArtifactService

# init
artifact_repo = ArtifactRepository(Artifact.objects)
artifact_service = ArtifactService(artifact_repo)
artifact_view = views.ArtifactAPIView.as_view(artifact_service=artifact_service)

urlpatterns = [
    path('artifact', artifact_view),
    path('artifact/<int:pk>', artifact_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
