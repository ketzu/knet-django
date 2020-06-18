from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from projects.models import Project


class ProjectList(ListView):
    model = Project
    ordering = ['-pk']
    template_name = "projects/project_list.html"