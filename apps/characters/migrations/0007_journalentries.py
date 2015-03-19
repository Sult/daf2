# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_auto_20150306_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('refid', models.BigIntegerField()),
                ('reftypeid', models.IntegerField()),
                ('ownername1', models.CharField(max_length=254)),
                ('ownerid1', models.IntegerField()),
                ('ownername2', models.CharField(max_length=254)),
                ('ownerid2', models.IntegerField()),
                ('argname1', models.CharField(max_length=254)),
                ('argid1', models.IntegerField()),
                ('amount', models.DecimalField(max_digits=19, decimal_places=2)),
                ('balance', models.DecimalField(max_digits=19, decimal_places=2)),
                ('reason', models.TextField(blank=True)),
                ('taxreceiverid', models.IntegerField()),
                ('taxamount', models.DecimalField(max_digits=19, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
