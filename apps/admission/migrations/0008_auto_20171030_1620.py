# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20171030_1301'),
        ('departement', '0006_auto_20171030_1341'),
        ('admission', '0007_auto_20171030_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='last_name',
        ),
        migrations.AddField(
            model_name='admission',
            name='academic_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.AcademicYear'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='departement.Department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='fees',
            field=models.IntegerField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]