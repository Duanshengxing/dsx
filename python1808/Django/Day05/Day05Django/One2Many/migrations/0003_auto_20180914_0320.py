# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-14 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('One2Many', '0002_auto_20180914_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='One2Many.UserType'),
        ),
    ]
