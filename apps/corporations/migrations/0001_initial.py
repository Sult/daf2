# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorporationApi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('corporationid', models.BigIntegerField()),
                ('corporationname', models.CharField(max_length=254)),
                ('api', models.OneToOneField(to='apies.Api')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
