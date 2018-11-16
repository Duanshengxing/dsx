from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index',index),
    url(r'^list',list,name='list'),
    url(r'^detail/(\w+)/',detail,name='detail'),
]