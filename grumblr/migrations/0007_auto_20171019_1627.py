# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0006_auto_20171019_0318'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
