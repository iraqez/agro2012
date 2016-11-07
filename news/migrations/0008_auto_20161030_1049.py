# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 08:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20161030_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='news', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 10, 30, 10, 49, 49, 892155), verbose_name='Опублікована'),
        ),
    ]