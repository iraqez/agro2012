# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 13:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_auto_20161030_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 10, 30, 15, 10, 28, 518900), verbose_name='Опублікована'),
        ),
    ]