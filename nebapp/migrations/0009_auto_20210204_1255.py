# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-02-04 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nebapp', '0008_auto_20210204_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='location',
            new_name='name',
        ),
    ]
