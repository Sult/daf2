# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0009_auto_20150305_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporation',
            name='alliancename',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 14, 34, 34, 863436, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
