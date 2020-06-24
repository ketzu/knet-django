from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView

from .models import Gallery, Image


class GalleryList(ListView):
    model = Gallery
    template_name = "photography/gallery_list.html"


class GalleryView(ListView):
    model = Image
    template_name = "photography/gallery.html"
    allow_empty = False

    def get_queryset(self, *args, **kwargs):
        gallery = get_object_or_404(Gallery, slug=self.kwargs['slug'])
        return Image.objects.filter(in_gallery_id=gallery.id)

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        gallery = get_object_or_404(Gallery, slug=self.kwargs['slug'])
        context['title'] = gallery.title
        context['slug'] = self.kwargs['slug']
        return context


@login_required
def upload(request, slug):
    if request.method == "POST":
        picture = request.FILES['image']
        if picture is not None:
            entry = Image()
            entry.picture = picture

            gallery = get_object_or_404(Gallery, slug=slug)
            entry.in_gallery = gallery

            entry.save()
            return HttpResponse('{"status": "200"}', content_type="application/json", status=200)
        return HttpResponse('{"status": "400", "details": "Picture is None"}', content_type="application/json", status=400)
    return HttpResponse('{"status": "400", "details": "None"}', content_type="application/json", status=400)
