from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View

from photography.models import Image, Gallery


@method_decorator(login_required, name='dispatch')
class ImageApi(View):

    def get(self, request, id, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)

    def post(self, request, id, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)

    def delete(self, request, id, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)

    def update(self, request, id, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)


@method_decorator(login_required, name='dispatch')
class GalleryApi(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)

    def post(self, request, slug, *args, **kwargs):
        picture = request.FILES['image']
        if picture is not None:
            entry = Image()
            entry.picture = picture

            gallery = Gallery.objects.get(slug=slug)
            if gallery is None:
                return HttpResponse('{"details": "Gallery is None"}', content_type="application/json", status=400)

            entry.in_gallery = gallery
            entry.save()
            return HttpResponse('', content_type="application/json", status=200)
        return HttpResponse('{"details": "Picture is None"}', content_type="application/json", status=400)

    def delete(self, request, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)

    def update(self, request, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)


@method_decorator(login_required, name='dispatch')
class ThumbnailApi(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)

    def post(self, request, slug, *args, **kwargs):
        gallery = Gallery.objects.get(slug=slug)
        if gallery is None:
            return HttpResponse('{"details": "Gallery is None"}', content_type="application/json", status=400)
        picture = Image.objects.get(pk=request.body)
        if picture is None:
            return HttpResponse('{"details": "Picture is None"}', content_type="application/json", status=400)
        gallery.thumbnail = picture
        gallery.save()
        return HttpResponse('', content_type="application/json", status=200)

    def delete(self, request, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)

    def update(self, request, *args, **kwargs):
        return HttpResponse('{"details": "None"}', content_type="application/json", status=400)