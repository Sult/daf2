# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0004_auto_20150226_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='alianceid',
            field=models.BigIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 17, 47, 31, 64580, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
