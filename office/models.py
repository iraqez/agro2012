from django.db import models

class Office(models.Model):
    OFFICE_TYPE = (
        ('CO', 'Головний офіс'),
        ('RO', 'Регіональний офіс'),
    )
    office_type = models.CharField(max_length=2, choices=OFFICE_TYPE, default='RO')
    TYPE_SITY =         (
        ('1', 'м.'),
        ('2', 'смт.'),
        ('3', 'с.'),
    )
    type_sity = models.CharField(max_length=1, choices=TYPE_SITY, default='м.')
    post_index = models.CharField(max_length=5, verbose_name='Поштовий індекс')
    country_name = models.CharField(max_length=150, verbose_name='Країна', default='Україна')
    region = models.CharField(max_length=150, verbose_name='Область', default='Хмельницька')
    sity_office = models.CharField(max_length=150, verbose_name='Населений пункт', default='Хмельницький')
    street = models.CharField(max_length=150, verbose_name='Вулиця')
    building = models.CharField(max_length=10, verbose_name='Номер будинку')
    phone = models.CharField(max_length=18, verbose_name='Номер телефону')
    email = models.EmailField()

    def __str__(self):
        return self.get_office_type_display() + ' ' + self.get_type_sity_display() + ' ' + self.sity_office

    class Meta:
        verbose_name = "офіс"
        verbose_name_plural = "офіси"