# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170307_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermember',
            name='token',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
