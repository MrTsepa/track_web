# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_path', models.CharField(max_length=256)),
                ('output_path', models.CharField(max_length=256)),
            ],
        ),
    ]
