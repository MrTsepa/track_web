# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='Task', max_length=256),
            preserve_default=False,
        ),
    ]
