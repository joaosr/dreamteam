# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170227_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermember',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Team'),
        ),
    ]
