from django.db import models

# Create your models here.
from stdimage import JPEGField


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = JPEGField(upload_to='projects/', variations={'full': (None, None), 'show': {'width': 500, 'height': 500, 'crop': True}}, null=True)
    link = models.CharField(max_length=500, null=True)
    git = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.name)
