from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index',index,name='index'),
    url(r'^login', login, name='login'),

    url(r'^register', register, name='register'),
    url(r'^check', check, name='check'),

]