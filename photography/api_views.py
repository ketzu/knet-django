from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.core import serializers

from photography.models import Image, Gallery


def json_response(content, status):
    return HttpResponse(serializers.serialize('json', content), content_type="application/json", status=status)


def json_success():
    return json_response("", 200)


def json_failure(message, status):
    return json_response({"details": message}, status)


class JsonView(View):
    def get(self, request, *args, **kwargs):
        return json_failure("Not Implemented", 501)

    def post(self, request, *args, **kwargs):
        return json_failure("Not Implemented", 501)

    def delete(self, request, *args, **kwargs):
        return json_failure("Not Implemented", 501)

    def update(self, request, *args, **kwargs):
        return json_failure("Not Implemented", 501)


@method_decorator(login_required, name='dispatch')
class ImageApi(JsonView):
    def delete(self, request, id, *args, **kwargs):
        image = Image.objects.get(pk=id)
        if image is None:
            return json_failure("Image not found", 400)
        image.delete()
        return json_success()


@method_decorator(login_required, name='dispatch')
class GalleryApi(JsonView):
    def post(self, request, slug, *args, **kwargs):
        picture = request.FILES['image']
        if picture is not None:
            entry = Image()
            entry.picture = picture

            gallery = Gallery.objects.get(slug=slug)
            if gallery is None:
                return json_failure("Gallery not found", 400)

            entry.in_gallery = gallery
            entry.save()
            return json_success()
        return json_failure("Image not found", 400)


@method_decorator(login_required, name='dispatch')
class GalleriesApi(JsonView):
    def post(self, request, *args, **kwargs):
        return json_failure("Not really implemented", 501)


@method_decorator(login_required, name='dispatch')
class ThumbnailApi(JsonView):
    def post(self, request, slug, *args, **kwargs):
        gallery = Gallery.objects.get(slug=slug)
        if gallery is None:
            return json_failure("Gallery not found", 400)
        picture = Image.objects.get(pk=request.body)
        if picture is None:
            return json_failure("Picture not found", 400)
        gallery.thumbnail = picture
        gallery.save()
        return json_success()
