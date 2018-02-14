# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 09:02
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0011_auto_20170228_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
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
    ]