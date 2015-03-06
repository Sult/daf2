# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20150226_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reftypeid', models.IntegerField(unique=True)),
                ('reftypename', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
