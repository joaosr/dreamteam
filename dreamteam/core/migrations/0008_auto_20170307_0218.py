# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170307_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermember',
            name='token',
            field=models.CharField(default='e0beb817865c49b1a70d6104748c12ed', max_length=32, unique=True),
        ),
    ]
