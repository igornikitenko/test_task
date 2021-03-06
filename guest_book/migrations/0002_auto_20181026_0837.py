# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-26 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='browser',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
