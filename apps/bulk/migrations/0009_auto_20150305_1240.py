# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0008_auto_20150302_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='employmenthistory',
            name='characterid',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='corporationid',
            field=models.BigIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 5, 12, 40, 2, 399859, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='employmenthistory',
            unique_together=set([('characterid', 'startdate')]),
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='character',
        ),
    ]
