# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dianping', '0006_auto_20170703_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='longtitude',
            new_name='longitude',
        ),
        migrations.RemoveField(
            model_name='business',
            name='has_online_reservation',
        ),
        migrations.RemoveField(
            model_name='business',
            name='has_takeaway',
        ),
        migrations.AddField(
            model_name='business',
            name='sale_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]
