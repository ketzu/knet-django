from django.urls import path
from .views import GalleryList, GalleryView, upload, set_thumbnail, remove_image

urlpatterns = [
    path('', GalleryList.as_view(), name='photo'),
    path('<slug:slug>/add', upload, name='add_picture'),
    path('<slug:slug>/thumb', set_thumbnail, name='set_thumbnail'),
    path('<slug:slug>/', GalleryView.as_view(), name='gallery'),
]
