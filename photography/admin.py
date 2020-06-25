from django.contrib import admin

# Register your models here.
from django import forms

from photography.models import Gallery, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('get_preview',)

    def get_preview(self, obj):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" height="100px"/>' % obj.picture.url)


class ImageStacked(admin.StackedInline):
    model = Image
    extra = 2


class GalleryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].queryset = Image.objects.filter(in_gallery=self.instance.pk)


class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageStacked]
    form = GalleryForm


admin.site.register(Gallery, GalleryAdmin)
