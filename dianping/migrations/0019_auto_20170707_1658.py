# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dianping', '0018_auto_20170707_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='review',
            name='excerpt',
            field=models.TextField(default=''),
        ),
    ]
