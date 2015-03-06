# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0002_auto_20150226_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 26, 19, 50, 35, 28386, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
