from django.conf.urls import url
from .views import *



urlpatterns = [
    url(r'index/',index,name='index'),
    url(r'^generate_verify/',generate_verify,name='generate_verify'),
]