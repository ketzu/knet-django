from django.contrib import admin

# Register your models here.
from .models import Article, Conference


admin.site.register(Conference)
admin.site.register(Article)
