# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Inappropriate', models.CharField(max_length=1)),
                ('Not_Helpful', models.CharField(max_length=1)),
                ('Wrong_Tags', models.CharField(max_length=1)),
                ('Spam', models.CharField(max_length=1)),
                ('product', models.ForeignKey(to='spotlight.Prod')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
