from django.conf.urls import url
from .views import *

urlpatterns = [
    # 首页
    url(r'^home/$', home, name='home'),

    # 闪购
    url(r'^market/$', market, name='market'),
    url(r'^marketwithparam/(\d+)/(\d+)/(\d+)/$', market_width_params, name='marketwithparam'),

    # 购物车
    url(r'^cart/$', cart, name='cart'),
    # 我的
    url(r'^mine/$', mine, name='mine'),
    url(r'^register/$',register,name='register'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^login/$',login,name='login'),
    url(r'^cart_add/$',cart_add,name='cart_add'),
    url(r'^cart_num_add/$',cart_num_add,name='cart_num_add'),
    url(r'^cart_num_reduce/$',cart_num_reduce,name='cart_num_reduce'),
    url(r'^cart_goods_del/$', cart_goods_del, name='cart_goods_del'),
    url(r'^select_status/$', select_status, name='select_status'),
    url(r'^cart_select_all/$', cart_select_all, name='cart_select_all'),

]


