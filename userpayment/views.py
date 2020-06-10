from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import *
from .forms import *
from .services import createPost, checkBalance


def userPageView(request):
    if request.user.is_authenticated:
        user = request.user.profile

        if request.method == 'POST':
            r = request.POST
            form = PayoutForm(r)

            if form.is_valid() and checkBalance(user.commission, r.get('sum')):
                payout = form.save(commit=False)
                payout.author = user

                if r.get('account_number'):
                    data = [
                        r.dict()['account_number'],
                        r.dict()['sum']
                        ]
                    createPost(data)

                payout.save()
                user.save()
                return redirect('/')
            else:
                messages.error(request, 'Your balance is smaller than payout sum')


        form = PayoutForm()
        context = {'user': user, 'form': form}
        return render(request, 'userpayment/user.html', context)
    else:
        return redirect('/admin/')





























# def register(request):
#     if request.method == 'POST':
#         form = ExtendedUserCreationForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#
#         if form.is_valid() and profile_form.is_valid():
#             user = form.save()
#
#             profile = profile_form.save()
#             profile = user
#
#             profile.save()
#
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             Profile.objects.create(user=user)
#             login(request, user)
#
#             return redirect('/')
#
#     else:
#         form = ExtendedUserCreationForm()
#         profile_form = ProfileForm()
#
#     context = {'form': form, 'profile_form': profile_form}
#     return render(request, 'userpayment/register.html', context)
