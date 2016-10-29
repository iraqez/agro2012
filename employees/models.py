from django.db import models
from image_cropping import ImageCropField, ImageRatioField
from django_resized import ResizedImageField
from sorl.thumbnail import get_thumbnail, ImageField

class Image(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title', blank=True)
    image = ImageField(blank=True, upload_to='employees')
    # size is "width x height"
    cropping = ImageRatioField('image', '600x600',  free_crop=True, size_warning=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "фото"