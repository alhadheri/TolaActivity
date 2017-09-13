# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0039_auto_20170913_0421'),
        ('indicators', '0011_indicator_sub_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datacollectionfrequency',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='historicalindicator',
            name='data_collection_frequency',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='data_collection_frequency',
        ),
        migrations.AddField(
            model_name='reportingfrequency',
            name='numdays',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Frequency in number of days'),
        ),
        migrations.AddField(
            model_name='reportingfrequency',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization'),
        ),
        migrations.DeleteModel(
            name='DataCollectionFrequency',
        ),
    ]
