# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
