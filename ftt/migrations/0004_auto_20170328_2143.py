# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 21:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftt', '0003_timer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Timer',
            new_name='Clock',
        ),
    ]