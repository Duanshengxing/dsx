from django.shortcuts import render
from .models import *


# 首页
def home(request):

    # 获取首页数据
    # 轮播数据
    wheels = MainWheel.objects.all()


    data = {
        "wheels": wheels,
    }

    # 渲染
    return render(request, 'home/home.html', context=data)


# 闪购
def market(request):
    return render(request, 'market/market.html')


# 购物车
def cart(request):
    return render(request, 'cart/cart.html')


# 我的
def mine(request):
    return render(request, 'mine/mine.html')

