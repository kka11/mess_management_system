# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0005_breakfast_dinner_lunch'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ID',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]