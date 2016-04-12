# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigtask', '0006_auto_20160411_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='Instrument',
            field=models.CharField(max_length=100, choices=[(b'p', b'piano'), (b'v', b'violin'), (b'g', b'guita'), (b'c', b'cello')]),
        ),
    ]
