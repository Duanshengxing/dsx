# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-14 08:07
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('One2One', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('m', django.db.models.manager.Manager()),
            ],
        ),
    ]
