# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0002_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='Inappropriate',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='flag',
            name='Not_Helpful',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='flag',
            name='Spam',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='flag',
            name='Wrong_Tags',
            field=models.CharField(max_length=12),
        ),
    ]
