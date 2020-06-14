from django.db import models

from stdimage import JPEGField


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    picture = JPEGField(upload_to='medium/', variations={'full': (None, None), 'thumbnail': {'width': 150, 'height': 100, 'crop': True}}, null=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.title
