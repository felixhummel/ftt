# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftt', '0004_auto_20170328_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='clock',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
