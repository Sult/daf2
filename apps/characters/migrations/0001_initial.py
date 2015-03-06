# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterApi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('characterid', models.BigIntegerField()),
                ('charactername', models.CharField(max_length=254)),
                ('corporationid', models.BigIntegerField()),
                ('corporationname', models.CharField(max_length=254)),
                ('api', models.ForeignKey(to='apies.Api')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RequiredSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skilllevel', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeid', models.BigIntegerField(unique=True)),
                ('typename', models.CharField(max_length=254)),
                ('published', models.IntegerField()),
                ('description', models.TextField()),
                ('rank', models.IntegerField()),
                ('primaryattribute', models.CharField(max_length=254)),
                ('secondaryattribute', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillBonus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bonustype', models.CharField(max_length=254)),
                ('bonusvalue', models.FloatField()),
                ('skill', models.ForeignKey(to='characters.Skill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupid', models.BigIntegerField(unique=True)),
                ('groupname', models.CharField(unique=True, max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='skill',
            name='skillgroup',
            field=models.ForeignKey(to='characters.SkillGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requiredskill',
            name='required',
            field=models.ForeignKey(related_name='required', to='characters.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requiredskill',
            name='skill',
            field=models.ForeignKey(related_name='required_skills', to='characters.Skill'),
            preserve_default=True,
        ),
    ]
