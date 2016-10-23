from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Image


class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)
