# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotes',
            name='users',
        ),
        migrations.AddField(
            model_name='quotes',
            name='poster',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]
