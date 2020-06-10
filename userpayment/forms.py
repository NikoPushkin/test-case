from django import forms
from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Payout

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('commission', 'phone_number')

class PayoutForm(forms.ModelForm):

    account_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'account-form'}))

    class Meta:
        model = Payout
        fields = ('sum',)
        widgets = {
            'sum': forms.NumberInput(attrs={'class': 'sum-form'}),
        }
