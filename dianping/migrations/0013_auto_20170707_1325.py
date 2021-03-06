# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 05:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dianping', '0012_auto_20170706_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='DianpingUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=35)),
                ('starred_list', models.ManyToManyField(to='dianping.Business')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='browsed_list',
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='dianping.DianpingUser'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='dianping.DianpingUser'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='dianpinguser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dianping_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to='dianping.DianpingUser'),
        ),
    ]
