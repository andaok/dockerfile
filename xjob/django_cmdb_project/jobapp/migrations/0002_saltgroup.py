# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-27 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaltGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupName', models.CharField(max_length=128, unique=True)),
                ('GroupExpr', models.TextField()),
            ],
        ),
    ]
