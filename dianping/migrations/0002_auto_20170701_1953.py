# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dianping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='business',
        ),
        migrations.AddField(
            model_name='business',
            name='popular_dishes',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
