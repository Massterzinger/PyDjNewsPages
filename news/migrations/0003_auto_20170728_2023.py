# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170728_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
