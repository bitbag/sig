# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigtask', '0009_album_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='status',
            field=models.CharField(default=4, max_length=30, choices=[(b'0', b'unexecuted'), (b'1', b'executing'), (b'2', b'executed'), (b'3', b'failed'), (b'4', b'unknown')]),
        ),
    ]
