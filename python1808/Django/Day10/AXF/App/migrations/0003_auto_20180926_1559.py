# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pwd',
            field=models.CharField(max_length=50),
        ),
    ]
