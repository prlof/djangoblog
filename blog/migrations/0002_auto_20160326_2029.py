# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoris',
            new_name='categories',
        ),
    ]
