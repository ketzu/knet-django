from django.urls import path
from .views import GalleryList, GalleryView

urlpatterns = [
    path('', GalleryList.as_view(), name='photo'),
    path('<slug:slug>/', GalleryView.as_view(), name='gallery'),
]
