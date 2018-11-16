from django.conf.urls import url
from .views import *

urlpatterns = [
    # 首页
    url(r'^home/$', home, name='home'),

    # 闪购
    url(r'^market/$', market, name='market'),
    # 购物车
    url(r'^cart/$', cart, name='cart'),
    # 我的
    url(r'^mine/$', mine, name='mine'),

]


