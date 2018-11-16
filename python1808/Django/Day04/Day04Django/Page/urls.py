from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^index/(\d+)/',index,name='index'),
    url('^test/',test)
]