# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-07 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191007_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='product',
            new_name='Product',
        ),
    ]
