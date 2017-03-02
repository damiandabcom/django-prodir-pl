# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170214_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='company',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='position',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]