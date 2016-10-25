#http://cowo.ks.ua/10-5.html

from django.db import models
from datetime import datetime
from django_resized import ResizedImageField
from sorl.thumbnail import get_thumbnail

class New(models.Model):
    image = models.ImageField(size=[850, 850], upload_to='news', verbose_name='Фото')
    title = models.CharField(max_length=150, unique_for_date='posted', verbose_name='Заголовок')
    content = models.TextField(verbose_name='Зміст')
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name='Опублікована')



    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-posted"]
        verbose_name = "новину"
        verbose_name_plural = "новини"