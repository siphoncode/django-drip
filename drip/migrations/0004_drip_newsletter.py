# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0003_drip_body_plain_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='drip',
            name='newsletter',
            field=models.BooleanField(default=False),
        ),
    ]