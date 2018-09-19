# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandasApp', '0004_auto_20180918_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrobandas',
            name='categoria',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
