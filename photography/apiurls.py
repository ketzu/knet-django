from django.urls import path
from .api_views import ThumbnailApi, ImageApi, GalleryApi

urlpatterns = [
    path('image/<int:id>', ImageApi.as_view(), name='picture_api'),
    path('gallery/<slug:slug>/thumbnail', ThumbnailApi.as_view(), name='thumbnail_api'),
    path('gallery/<slug:slug>', GalleryApi.as_view(), name='gallery_api'),
]
