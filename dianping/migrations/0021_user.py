# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dianping', '0020_auto_20170708_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
            ],
        ),
    ]