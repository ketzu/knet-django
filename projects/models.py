from django.db import models

# Create your models here.
from stdimage import StdImageField


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = StdImageField(upload_to='projects/', variations={'show': {'width': 285, 'height': 285, 'crop': True}}, null=True)
    link = models.CharField(max_length=500, null=True)
    git = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.name)
