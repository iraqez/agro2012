# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 19:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 10, 28, 22, 49, 57, 140500), verbose_name='Опублікована'),
        ),
    ]
