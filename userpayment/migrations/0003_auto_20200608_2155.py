# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-08 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userpayment', '0002_auto_20200608_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='adas@sad.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='userpayment.Profile'),
        ),
    ]
