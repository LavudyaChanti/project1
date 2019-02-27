from django.contrib import admin
from django.conf.urls import url
from employee.views import *
urlpatterns = [
    url(r'^$',home),
    url(r'home/',home,name='home'),
    url(r'reg/',reg,name='reg'),
    url(r'show/',show,name='show'),
    url(r'delete/',delete,name='delete'),
    url(r'deleteprocess/',deleteprocess,name='deleteprocess'),
    url(r'regprocess/',regprocess,name='regprocess'),
    url(r'regerror/',regerror,name='regerror'),
    url(r'regsuccess/',regsuccess,name='regsuccess'),
    url(r'admin/', admin.site.urls),
]
