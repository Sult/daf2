# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import config.storage


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterIcon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.IntegerField(choices=[(b'Tiny', 32), (b'Small', 64), (b'Medium', 128), (b'Large', 256), (b'Huge', 512), (b'Special', 200)])),
                ('typeid', models.IntegerField(unique=True)),
                ('icon', models.ImageField(storage=config.storage.OverwriteStorage(), null=True, upload_to=b'images/characters/', blank=True)),
                ('relation', models.ForeignKey(to='characters.CharacterApi')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='charactericon',
            unique_together=set([('size', 'relation')]),
        ),
    ]
