# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('key', models.IntegerField(verbose_name=b'Key ID')),
                ('vcode', models.CharField(max_length=254, verbose_name=b'Verification Code')),
                ('accounttype', models.CharField(max_length=254, choices=[(b'Character', b'Character'), (b'Account', b'Account'), (b'Corporation', b'Corporation')])),
                ('expires', models.DateTimeField(null=True)),
                ('accessmask', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accessmask', models.IntegerField()),
                ('accounttype', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CallGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupid', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='call',
            name='callgroup',
            field=models.ForeignKey(to='apies.CallGroup'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='call',
            unique_together=set([('accounttype', 'name')]),
        ),
    ]
