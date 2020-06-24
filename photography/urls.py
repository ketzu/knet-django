from django.urls import path
from .views import GalleryList, GalleryView, upload

urlpatterns = [
    path('', GalleryList.as_view(), name='photo'),
    path('<slug:slug>/add', upload, name='add_picture'),
    path('<slug:slug>/', GalleryView.as_view(), name='gallery'),
]
