from django.db import models
from image_cropping import ImageCropField, ImageRatioField
# from django_resized import ResizedImageField
# from sorl.thumbnail import get_thumbnail

class Image(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title', blank=True)
    image = ImageCropField(blank=True, upload_to='img')
    # size is "width x height"
    cropping = ImageRatioField('image', '600x600',  free_crop=False, size_warning=True)

    class Meta:
        verbose_name = "Фото"