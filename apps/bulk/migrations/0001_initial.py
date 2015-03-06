# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=254)),
                ('shortname', models.CharField(max_length=254)),
                ('allianceid', models.BigIntegerField(unique=True)),
                ('executorcorpid', models.BigIntegerField(unique=True)),
                ('membercount', models.IntegerField()),
                ('startdate', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastrefresh', models.DateTimeField(null=True)),
                ('characterid', models.BigIntegerField(unique=True)),
                ('charactername', models.CharField(unique=True, max_length=254)),
                ('corporationid', models.BigIntegerField()),
                ('corporationname', models.CharField(max_length=254, blank=True)),
                ('corporationdate', models.DateTimeField(null=True)),
                ('alliancedate', models.DateTimeField(null=True)),
                ('securitystatus', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastrefresh', models.DateTimeField(null=True)),
                ('corporationid', models.BigIntegerField(unique=True)),
                ('corporationname', models.CharField(unique=True, max_length=254)),
                ('ticker', models.CharField(max_length=254)),
                ('isnpccorp', models.BooleanField(default=False)),
                ('allianceid', models.BigIntegerField(null=True)),
                ('alliancename', models.CharField(max_length=254)),
                ('avgsecstatus', models.FloatField(default=0.0)),
                ('ceoid', models.BigIntegerField()),
                ('ceoname', models.CharField(max_length=254)),
                ('stationid', models.BigIntegerField()),
                ('description', models.TextField()),
                ('url', models.URLField(max_length=254)),
                ('taxrate', models.FloatField()),
                ('membercount', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('corporationid', models.IntegerField()),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField(null=True)),
                ('character', models.ForeignKey(to='bulk.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sovereignty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solarsystemid', models.BigIntegerField(unique=True)),
                ('solarsystemname', models.CharField(unique=True, max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SovereigntyHolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_refresh', models.DateTimeField(default=datetime.datetime(2015, 2, 25, 15, 26, 34, 220727, tzinfo=utc))),
                ('allianceid', models.BigIntegerField(null=True)),
                ('corporationid', models.BigIntegerField(null=True)),
                ('factionid', models.BigIntegerField(null=True)),
                ('sovereignty', models.ForeignKey(to='bulk.Sovereignty')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
