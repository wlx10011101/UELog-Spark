# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UELogApp', '0008_auto_20170707_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultrecord',
            name='isfPath',
            field=models.FilePathField(path='/home/wlx/Pictures', recursive=True),
        ),
        migrations.AlterField(
            model_name='resultrecord',
            name='resultPath',
            field=models.FilePathField(path='/home/wlx/Pictures', recursive=True),
        ),
    ]
