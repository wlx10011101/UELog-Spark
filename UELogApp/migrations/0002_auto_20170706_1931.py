# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UELogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='uuId',
            field=models.UUIDField(default=None),
        ),
    ]
