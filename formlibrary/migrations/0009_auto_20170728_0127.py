# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0002_auto_20170707_0539'),
        ('formlibrary', '0008_auto_20170728_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingattendance',
            name='training_indicator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indicators.Indicator'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='distribution_indicator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indicators.Indicator'),
        ),
    ]