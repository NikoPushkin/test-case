from .models import *
import requests


def createPayment(id, sum):
    user = Profile.objects.get(id=id)
    payment = Payment(author=user, sum=sum)
    payment.save()
    user.save()
    return "Payment by {} {} was created".format(user.firstname, user.lastname)

def withdraw(queryset):
    for i in queryset:
        i.author.commission -= i.sum
        i.author.save()

def createPost(data):
    url = 'https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4'
    obj = {'account': "{}".format(data[0]), 'amount': float(data[1])}
    r = requests.post(url, data=obj)
    return r

def checkBalance(commission, sum):
    if float(sum) <= (commission):
        return True
    return False
