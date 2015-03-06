# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=62)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('body', froala_editor.fields.FroalaField()),
                ('public', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=False)),
                ('sticky', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('corp', models.BooleanField(default=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(max_length=1000)),
                ('article', models.ForeignKey(to='blog.Article')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('reply_to', models.ForeignKey(to='blog.Comment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
