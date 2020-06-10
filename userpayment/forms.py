from django import forms
from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Payout


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'password1', 'password2'
            )

        def save(self, commit=True):
            user = super().save(commit=False)

            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']

            if commit:
                user.save()
            return user

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
