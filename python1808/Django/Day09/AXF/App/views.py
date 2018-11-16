from django.shortcuts import render
from .models import *
# Create your views here.


#首页
def home(request):
    #获取首页数据
    #轮播数据
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    # 必购数据
    mustbuys = Mustbuy.objects.all()
    # shop数据
    shops = Shop.objects.all()

    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shops':shops,
    }
    return render(request,'home/home.html',data)


#闪购
def market(request):

    return render(request,'market/market.html')

#购物车
def cart(request):

    return render(request,'cart/cart.html')


#我的
def mine(request):

    return render(request,'mine/mine.html')

