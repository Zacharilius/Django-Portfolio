# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20151031_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='MushroomSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('geom', djgeojson.fields.PointField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
