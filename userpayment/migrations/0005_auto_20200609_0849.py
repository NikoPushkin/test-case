# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-09 08:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpayment', '0004_auto_20200608_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='sum',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='payout',
            name='sum',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='commission',
            field=models.FloatField(default=0),
        ),
    ]
