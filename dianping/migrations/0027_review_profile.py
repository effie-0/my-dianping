# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dianping', '0026_auto_20170708_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to='dianping.Profile'),
        ),
    ]
