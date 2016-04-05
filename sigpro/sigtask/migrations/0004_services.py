# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigtask', '0003_auto_20160401_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serviceid', models.CharField(max_length=15)),
                ('servicename', models.CharField(max_length=30)),
                ('serviceversion', models.CharField(max_length=30)),
                ('serviceport', models.IntegerField()),
            ],
        ),
    ]
