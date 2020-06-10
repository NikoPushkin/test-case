from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from decimal import Decimal


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    commission = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

class Payment(models.Model):
    author = models.ForeignKey(Profile, related_name='profile' ,on_delete=models.CASCADE)
    sum = models.DecimalField(decimal_places=2, max_digits=19, validators=[MinValueValidator(0.01)])
    date = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        self.author.commission += Decimal(self.sum * 0.3)
        super().save(*args, **kwargs)


class Payout(models.Model):
    author = models.ForeignKey(Profile, related_name='payer' ,on_delete=models.CASCADE)
    sum = models.DecimalField(decimal_places=2, max_digits=19, validators=[MinValueValidator(0.01)])
    request_date = models.DateTimeField(default=datetime.now)
    processing_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
