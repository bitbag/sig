# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('Release_date', models.DateField()),
                ('Num_starts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Instrument', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='Artist',
            field=models.ForeignKey(to='sigtask.Musician'),
        ),
    ]
