# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-12 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('type', models.TextField()),
                ('price', models.TextField()),
                ('status', models.TextField()),
                ('marca', models.TextField()),
                ('date', models.TextField()),
                ('picture', models.TextField()),
                ('description', models.TextField()),
                ('shop', models.TextField()),
            ],
            options={
                'ordering': ('type',),
            },
        ),
    ]
