# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flashTrolley', '0005_auto_20150922_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fname',
            field=models.CharField(max_length=25, verbose_name=b'First Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lname',
            field=models.CharField(max_length=25, verbose_name=b'Last Name'),
        ),
    ]
