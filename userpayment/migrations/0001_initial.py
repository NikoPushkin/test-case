# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-08 19:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.DecimalField(decimal_places=3, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Payout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.DecimalField(decimal_places=3, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('request_date', models.DateTimeField(default=datetime.datetime.now)),
                ('processing_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='payout',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userpayment.Profile'),
        ),
        migrations.AddField(
            model_name='payment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userpayment.Profile'),
        ),
    ]