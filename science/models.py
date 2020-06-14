from django.db import models

# Create your models here.


class Conference(models.Model):
    name = models.CharField(max_length=200)
    short = models.CharField(max_length=20)

    def __str__(self):
        return self.short


class Article(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    file = models.FileField(upload_to='science/')
    conf = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
