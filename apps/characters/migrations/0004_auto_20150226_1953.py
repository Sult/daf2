# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20150226_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterapiicon',
            name='typeid',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
