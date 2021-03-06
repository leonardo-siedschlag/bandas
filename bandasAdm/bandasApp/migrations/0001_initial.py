# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeBanda', models.CharField(unique=True, max_length=128)),
                ('tempoCarreira', models.IntegerField(max_length=30)),
                ('dataFundacao', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
