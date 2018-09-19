# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandasApp', '0003_auto_20180918_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrobandas',
            name='dataFundacao',
            field=models.DateField(null=True),
        ),
    ]
