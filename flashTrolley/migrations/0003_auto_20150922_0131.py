# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flashTrolley', '0002_auto_20150922_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2015, 9, 21, 22, 30, 45, 354000, tzinfo=utc), max_length=30, verbose_name=b'First name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2015, 9, 21, 22, 30, 58, 851000, tzinfo=utc), max_length=30, verbose_name=b'Last name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=datetime.datetime(2015, 9, 21, 22, 31, 13, 130000, tzinfo=utc), max_length=30, verbose_name=b'User name'),
            preserve_default=False,
        ),
    ]
