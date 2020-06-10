from django.conf.urls import url, include
from django.contrib import admin

from .views import redirectPage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', redirectPage),
    url(r'user/', include('userpayment.urls')),
]
