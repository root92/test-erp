# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_academicyear_school_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_name',
            field=models.CharField(max_length=100),
        ),
    ]
