# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('piktogram', models.CharField(max_length=255)),
                ('legenda', models.CharField(max_length=255)),
                ('sifra', models.CharField(max_length=255)),
                ('naziv_hemikalije', models.CharField(max_length=255)),
                ('oficinalno', models.CharField(max_length=255)),
                ('jedinica', models.CharField(max_length=255)),
                ('cena', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
