# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-02-04 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nebapp', '0006_auto_20210204_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='house_rooms',
            new_name='bed_rooms',
        ),
    ]
