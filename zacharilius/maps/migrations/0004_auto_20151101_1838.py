# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_mushroomspot'),
    ]

    operations = [
        migrations.AddField(
            model_name='mushroomspot',
            name='description',
            field=models.TextField(default='mushroom.jpeg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mushroomspot',
            name='picture',
            field=models.ImageField(default='mushroom.jpeg', upload_to=''),
            preserve_default=False,
        ),
    ]
