# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dianping', '0025_profile_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='starred_list',
            field=models.ManyToManyField(default=None, to='dianping.Business'),
        ),
    ]
