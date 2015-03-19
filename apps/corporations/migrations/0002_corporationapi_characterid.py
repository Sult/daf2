# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corporations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='corporationapi',
            name='characterid',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
