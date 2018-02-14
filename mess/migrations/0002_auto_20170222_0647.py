# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 06:47
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mess.UserProfile')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('mess.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='feedBack',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='vendor',
            name='stud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mess.Student'),
        ),
    ]
