# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flashTrolley', '0004_auto_20150922_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=datetime.datetime(2015, 9, 22, 3, 49, 45, 489000, tzinfo=utc), max_length=30, verbose_name=b'User name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='fname',
            field=models.CharField(max_length=20, verbose_name=b'First Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lname',
            field=models.CharField(max_length=20, verbose_name=b'Last Name'),
        ),
    ]
