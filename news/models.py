from django.db import models
from datetime import datetime
from django_resized import ResizedImageField
from sorl.thumbnail import get_thumbnail

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва категорії')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "категорія"
        verbose_name_plural = "категорії"

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва тегу")
    def __str__(self):
        return self.name
    class Meta:
            verbose_name = "тег"
            verbose_name_plural = "теги"

class New(models.Model):
    image = ResizedImageField(size=[850, 850], upload_to='news', verbose_name='Фото')
    title = models.CharField(max_length=150, unique_for_date='posted', verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Адресна строка')
    content = models.TextField(verbose_name='Зміст')
    category = models.ForeignKey(Category, verbose_name='Оберіть категорію')
    tag = models.ManyToManyField(Tag, verbose_name='Оберіть теги для статті')
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name='Опублікована')

    def get_thumbnail_html(self):
        img = self.image
        img_resize_url = str(get_thumbnail(img, '100x100').url)
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.image.url, img_resize_url, self.title)
    get_thumbnail_html.short_description = u'Миниатюра'
    get_thumbnail_html.allow_tags = True

    def get_absolute_url(self):
        return "/news/%s/" % self.slug

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-posted"]
        verbose_name = "новину"
        verbose_name_plural = "новини"
