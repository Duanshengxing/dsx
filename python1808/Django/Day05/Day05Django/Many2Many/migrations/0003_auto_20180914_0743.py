# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-14 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Many2Many', '0002_auto_20180914_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='boy_num',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='girl_num',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
