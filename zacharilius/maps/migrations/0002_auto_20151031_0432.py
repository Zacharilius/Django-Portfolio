# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breweries',
            name='latitude',
            field=models.FloatField(verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='breweries',
            name='longitude',
            field=models.FloatField(verbose_name='longitude'),
        ),
        migrations.AlterField(
            model_name='breweries',
            name='title',
            field=models.CharField(max_length=128, verbose_name='title'),
        ),
    ]
