# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-09 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_activeacademicyear'),
        ('admission', '0020_auto_20171209_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='active_year',
            field=models.ForeignKey(default=1, max_length=32, on_delete=django.db.models.deletion.CASCADE, to='school.ActiveAcademicYear'),
            preserve_default=False,
        ),
    ]