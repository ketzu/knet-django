from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from .models import Gallery, Image


class GalleryList(ListView):
    model = Gallery
    template_name = "photography/gallery_list.html"


class GalleryView(ListView):
    model = Image
    template_name = "photography/gallery.html"
    allow_empty = True

    def get_queryset(self, *args, **kwargs):
        gallery = get_object_or_404(Gallery, slug=self.kwargs['slug'])
        return Image.objects.filter(in_gallery_id=gallery.id)

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        gallery = get_object_or_404(Gallery, slug=self.kwargs['slug'])
        context['title'] = gallery.title
        context['slug'] = self.kwargs['slug']
        if gallery.thumbnail is not None:
            context['thumb_pk'] = gallery.thumbnail.pk
        else:
            context['thumb_pk'] = -1
        return context
