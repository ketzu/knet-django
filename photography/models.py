from django.contrib import admin
from django.db import models

# Create your models here.
from django.utils.text import slugify
from stdimage import JPEGField


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ForeignKey('Image', null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save()


class Image(models.Model):
    picture = JPEGField(upload_to='gallery/', variations={'full': (None, None), 'thumbnail': {'height': 200}, 'big_thumbnail': {'width': 360}}, null=True)
    in_gallery = models.ForeignKey(Gallery, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.picture.name
