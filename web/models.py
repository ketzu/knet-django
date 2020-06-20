from django.db import models

# Create your models here.
from medium.models import Article as MediumArticle
from photography.models import Gallery
from projects.models import Project
from science.models import Article as ScienceArticle
from videography.models import Video


class FrontIcons(models.Model):
    icon = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
        return str(self.icon)


class FrontText(models.Model):
    paragraph = models.TextField()

    def __str__(self):
        return str(self.paragraph[:50])


class FrontScience(models.Model):
    article = models.ForeignKey(ScienceArticle, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.article)


class FrontMedium(models.Model):
    article = models.ForeignKey(MediumArticle, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.article)


class FrontGallery(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.gallery)


class FrontVideo(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.video)


class FrontProjects(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project)
