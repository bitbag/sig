# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigtask', '0008_auto_20160412_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='status',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
