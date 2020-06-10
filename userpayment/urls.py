from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url(r'^$', userPageView, name="userPageUrl"),
    # url(r'^registration/', register, name="registerUrl")
]
