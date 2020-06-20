from django.shortcuts import render

# Create your views here.
from .models import FrontMedium, FrontScience, FrontGallery, FrontVideo, FrontText, FrontIcons, FrontProjects


def overview(request):
    icons = [_ for _ in FrontIcons.objects.all()]
    paragraphs = [_.paragraph for _ in FrontText.objects.all()]
    science = [_.article for _ in FrontScience.objects.all()]
    medium = [_.article for _ in FrontMedium.objects.all()]
    galleries = [_.gallery for _ in FrontGallery.objects.all()]
    videos = [_.video for _ in FrontVideo.objects.all()]
    projects = [_.project for _ in FrontProjects.objects.all()]
    return render(request, "web/web.html", context={
        'icons': icons,
        'paragraphs': paragraphs,
        'projects': projects,
        'science': science,
        'medium': medium,
        'videos': videos,
        'galleries': galleries})
