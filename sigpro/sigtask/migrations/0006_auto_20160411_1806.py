# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigtask', '0005_auto_20160411_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Num_starts',
            field=models.IntegerField(default=2),
        ),
    ]
