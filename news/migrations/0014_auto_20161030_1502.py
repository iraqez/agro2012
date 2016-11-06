# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 13:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20161030_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорія', 'verbose_name_plural': 'категорії'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'тег', 'verbose_name_plural': 'теги'},
        ),
        migrations.AddField(
            model_name='new',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Назва категорії'),
        ),
        migrations.AlterField(
            model_name='new',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='Оберіть категорію'),
        ),
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 10, 30, 15, 2, 15, 317557), verbose_name='Опублікована'),
        ),
        migrations.AlterField(
            model_name='new',
            name='tag',
            field=models.ManyToManyField(to='news.Tag', verbose_name='Оберіть теги для статті'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Назва тегу'),
        ),
    ]
