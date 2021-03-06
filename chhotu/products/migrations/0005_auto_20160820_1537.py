# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Product Unique ID'),
        ),
    ]
