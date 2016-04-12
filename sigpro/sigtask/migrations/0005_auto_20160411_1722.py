# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigtask', '0004_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='status',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='musician',
            name='version',
            field=models.CharField(default=None, max_length=65),
        ),
    ]
