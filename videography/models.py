from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    description = models.TextField(default='')

    def __str__(self):
        return self.title
