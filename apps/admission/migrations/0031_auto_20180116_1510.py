# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-16 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0030_auto_20180116_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='active_year',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='class_level',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='registree',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='user',
        ),
        migrations.DeleteModel(
            name='Inscription',
        ),
    ]