# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flashTrolley', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='birth_date',
            new_name='dob',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 21, 21, 35, 53, 376000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(default=datetime.datetime(2015, 9, 21, 21, 36, 17, 159000, tzinfo=utc), max_length=20, verbose_name=b'Gender', choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='picture',
            field=models.ImageField(upload_to=b'flashTrolley/static/images/customers/profile_images', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=200, verbose_name=b'Country', choices=[(b'Ug', b'Uganda'), (b'Ke', b'Kenya'), (b'Tz', b'Tanzania')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=200, verbose_name=b'Phone Number'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to=b'flashTrolley/static/images/products'),
        ),
    ]
