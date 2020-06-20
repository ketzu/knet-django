from django.contrib import admin

# Register your models here.
from photography.models import Gallery, Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('get_preview',)

    def get_preview(self, obj):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" height="100px"/>' % obj.picture.url)


class ImageStacked(admin.StackedInline):
    model = Image
    extra = 20


class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageStacked]


admin.site.register(Gallery, GalleryAdmin)
