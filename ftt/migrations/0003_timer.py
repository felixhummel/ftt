# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftt', '0002_auto_20170328_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_dt', models.DateTimeField()),
                ('end_dt', models.DateTimeField(null=True)),
            ],
        ),
    ]