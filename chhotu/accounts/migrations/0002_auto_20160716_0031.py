# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name'),
        ),
    ]
