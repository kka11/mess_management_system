# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0009_auto_20170228_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feedback',
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedbac',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='feedBack',
            field=models.ManyToManyField(to='mess.Feedback'),
        ),
    ]
