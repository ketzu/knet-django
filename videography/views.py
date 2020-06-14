from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from videography.models import Video


class VideoList(ListView):
    model = Video
    template_name = "videography/video_list.html"
