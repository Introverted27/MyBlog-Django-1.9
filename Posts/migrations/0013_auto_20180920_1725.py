# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-09-20 11:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0012_auto_20180713_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2018, 9, 20, 11, 55, 13, 800297, tzinfo=utc)),
        ),
    ]
