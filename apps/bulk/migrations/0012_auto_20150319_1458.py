# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0011_auto_20150306_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 14, 57, 52, 533141, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
