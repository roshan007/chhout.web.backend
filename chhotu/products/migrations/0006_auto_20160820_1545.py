# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160820_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='status',
            new_name='availability',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[(b'PRT', b'Paratha'), (b'MGG', b'Maggie'), (b'BRG', b'Burger'), (b'SNW', b'Sandwich'), (b'TST', b'Toast'), (b'BVR', b'Beverage'), (b'OTH', b'Other')], max_length=2, verbose_name='Product Category'),
        ),
    ]