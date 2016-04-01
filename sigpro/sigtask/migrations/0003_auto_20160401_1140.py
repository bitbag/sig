# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigtask', '0002_auto_20160401_1136'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Muscian',
            new_name='Musician',
        ),
    ]
