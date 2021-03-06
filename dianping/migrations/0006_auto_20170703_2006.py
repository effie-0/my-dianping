# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dianping', '0005_auto_20170703_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='bussiness',
            new_name='business',
        ),
        migrations.AddField(
            model_name='review',
            name='author_id',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='review',
            name='photo_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='review',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='excertpt',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='grade',
            field=models.FloatField(default=-1),
        ),
    ]
