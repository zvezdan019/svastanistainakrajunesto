# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sifra', models.CharField(max_length=255)),
                ('naziv_medjuproizvoda', models.CharField(max_length=255)),
                ('oficinalno', models.CharField(max_length=255)),
                ('jedinica', models.CharField(max_length=255)),
                ('radna_tg', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
