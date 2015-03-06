# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0005_auto_20150302_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='alianceid',
            new_name='allianceid',
        ),
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 2, 17, 50, 40, 561187, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
