# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breweries',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('streetAddress', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
