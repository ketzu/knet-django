from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Article


class ArticleList(ListView):
    model = Article
    template_name = "science/article_list.html"
