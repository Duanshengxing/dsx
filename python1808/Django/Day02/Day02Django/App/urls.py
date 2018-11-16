from django.conf.urls import url

from App.views import *

urlpatterns = [
    url('^index/',index,name='index'),
    url('^detail/(\d)/',detail,name='detail'),
    url('^detail2/(\d)/(\d)/',detail2,name='detail2'),
    url('^detail3/(?P<id1>\d)/(?P<id2>\d)/',detail3,name='detail3'),
    url('^success/',success)
]