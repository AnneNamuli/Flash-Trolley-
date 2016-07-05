# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flashTrolley', '0006_auto_20150923_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=datetime.datetime(2015, 9, 23, 6, 44, 10, 859000, tzinfo=utc), max_length=30, verbose_name=b'username'),
            preserve_default=False,
        ),
    ]
