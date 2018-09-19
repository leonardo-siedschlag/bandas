# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandasApp', '0002_auto_20180911_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrobandas',
            name='tempoCarreira',
            field=models.IntegerField(max_length=30, null=True),
        ),
    ]
