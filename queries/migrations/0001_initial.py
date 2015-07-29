# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FishQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('location_id', models.IntegerField()),
                ('species', models.CharField(max_length=200)),
                ('species_id', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Fish Queries',
            },
        ),
    ]
