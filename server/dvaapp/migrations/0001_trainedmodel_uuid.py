# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-08 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', 'custom_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainedmodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
