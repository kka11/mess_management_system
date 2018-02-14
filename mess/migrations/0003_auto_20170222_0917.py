# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0002_auto_20170222_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='stud',
        ),
        migrations.AddField(
            model_name='student',
            name='stud',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mess.Vendor'),
        ),
        migrations.AlterField(
            model_name='student',
            name='feedBack',
            field=models.CharField(max_length=250, null=True),
        ),
    ]