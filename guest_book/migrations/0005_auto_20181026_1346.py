# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-26 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0004_auto_20181026_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]