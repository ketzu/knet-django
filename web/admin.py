from django.contrib import admin

# Register your models here.
from web.models import FrontMedium, FrontScience, FrontVideo, FrontGallery, FrontText, FrontIcons

admin.site.register(FrontIcons)
admin.site.register(FrontText)
admin.site.register(FrontScience)
admin.site.register(FrontMedium)
admin.site.register(FrontGallery)
admin.site.register(FrontVideo)
