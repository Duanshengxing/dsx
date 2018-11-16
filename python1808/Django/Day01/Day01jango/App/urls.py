from django.conf.urls import url
from .views import *


urlpatterns = [
    url('^welcome/',welcome),
    url('^love/',love),
    url('^grade/',grade),
    url('^showtime/',showtime),
    url('^show_stu/',show_stu)
]