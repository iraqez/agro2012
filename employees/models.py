from django.db import models
from image_cropping import ImageRatioField
from django_resized import ResizedImageField
from sorl.thumbnail import get_thumbnail

class MyModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title', blank=True)
    image = models.ImageField(blank=True, upload_to='uploaded_images')
    # size is "width x height"
    cropping = ImageRatioField('image', '200 x 200')


