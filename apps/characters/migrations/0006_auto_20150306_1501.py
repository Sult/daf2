# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_reftypes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RefTypes',
            new_name='RefType',
        ),
    ]
