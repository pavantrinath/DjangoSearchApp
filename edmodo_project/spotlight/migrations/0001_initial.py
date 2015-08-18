# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('store_url', models.URLField()),
                ('thumb_url', models.URLField()),
                ('edmodo_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('_index', models.CharField(max_length=128)),
                ('_type', models.CharField(max_length=128)),
                ('_score', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('currency', models.CharField(max_length=128)),
                ('min_price', models.IntegerField(default=0)),
                ('num_raters', models.IntegerField(default=0)),
                ('creation_date', models.DateField()),
                ('avg_rating', models.IntegerField(default=0)),
                ('seller_thumb_url', models.URLField()),
                ('title', models.CharField(max_length=128)),
                ('img_path', models.URLField()),
                ('greads_review_url', models.URLField()),
                ('owner', models.ForeignKey(to='spotlight.Owner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='prod',
            name='source',
            field=models.ForeignKey(to='spotlight.Source'),
            preserve_default=True,
        ),
    ]
