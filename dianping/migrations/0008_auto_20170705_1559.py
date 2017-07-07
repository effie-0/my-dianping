# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dianping', '0007_auto_20170704_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='excertpt',
        ),
        migrations.AddField(
            model_name='review',
            name='excerpt',
            field=models.CharField(default='', max_length=53),
        ),
        migrations.AlterField(
            model_name='business',
            name='avg_rating',
            field=models.FloatField(default=-1),
        ),
    ]