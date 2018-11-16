from django.http import JsonResponse
from django.shortcuts import *

from AXF.settings import MEDIA_ROOT
from .models import *
import uuid
import hashlib
import os
# 首页
def home(request):

    # 获取首页数据
    # 轮播数据
    wheels = MainWheel.objects.all()
    # 导航数据
    navs = MainNav.objects.all()
    # 必购数据
    mustbuys = MainMustbuy.objects.all()
    # shop数据
    shops = MainShop.objects.all()
    shops0 = shops.first()
    shops1_2 = shops[1:3]
    shops3_6 = shops[3:7]
    shops7_10 = shops[7:11]
    # 显示的商品数据
    mainshows = MainShow.objects.all()

    data = {
        "wheels": wheels,
        "navs": navs,
        "mustbuys": mustbuys,
        "shops0": shops0,
        "shops1_2": shops1_2,
        "shops3_6": shops3_6,
        "shops7_10": shops7_10,
        "mainshows": mainshows,
    }

    # 渲染
    return render(request, 'home/home.html', context=data)


# 闪购
def market(request):
    return redirect(reverse('AXF:marketwithparam',args=['104749','0','0']))

def market_width_params(request,typeid,childcid,sort_id):

    #获取分类数据
    foodtypes = FoodType.objects.all()

    # 获取数据
    goods_list = Goods.objects.filter(categoryid=typeid)
    if childcid != '0':
        goods_list = goods_list.filter(childcid=childcid)

    # 获取当前主分类下的子分类数据
    child_foodtype = foodtypes.filter(typeid=typeid).first()
    child_foodtype_str = child_foodtype.childtypenames
    child_type_list = child_foodtype_str.split('#')
    childtypes = []
    for string in child_type_list:
        name, id = string.split(':')
        childtypes.append({'childtypename': name, 'childtypeid': id})

    #获得综合排序下的子排序数据
    sort_types = [{'sort_name':'综合排序','sort_id':'0'},{'sort_name':'销量排序','sort_id':'1'},{'sort_name':'价格降序','sort_id':'2'},{'sort_name':'价格升序','sort_id':'3'}]
    if sort_id == '1':
        goods_list = goods_list.order_by('productnum')
    elif sort_id == '2':
        goods_list = goods_list.order_by('-price')
    elif sort_id == '3':
        goods_list = goods_list.order_by('price')
    else:
        pass


    data = {
        "foodtypes":foodtypes,
        'goods_list':goods_list,
        'typeid':typeid,
        'childtypes':childtypes,
        'sort_types':sort_types,
        'childcid':childcid,
    }





    return render(request, 'market/market.html',data)


# 购物车
def cart(request):
    #先判断是否登录
    userid = request.session.get('userid',0)
    if not userid:
        return redirect(reverse('AXF:login'))
    # 如果登录了，则获取当前购物车商品
    carts = Cart.objects.filter(user_id=userid)



    return render(request, 'cart/cart.html',{'carts':carts})


# 我的
def mine(request):
    # 获取当前用户的信息
    data = {
        'name':'',
        'icon':'',
    }
    userid = request.session.get('userid',0)
    users = User.objects.filter(id=userid)
    if users.exists():
        data['name'] = users.first().name
        data['icon'] = users.first().icon
    return render(request, 'mine/mine.html',data)

# 注册
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        email = request.POST.get('email')
        icon = request.FILES.get('file')

        # 验证
        if len(username) < 6:
            data = {
                'msg':'用户名长度至少为6位'

            }
            return render(request, 'user/register.html',data)

        # 注册
        user = User()
        user.name = username
        user.pwd = password
        user.email = email
        if icon:
            #将图片存入后台
            icon_name = generate_icon() + os.path.splitext(icon.name)[-1]
            icon_path = os.path.join(MEDIA_ROOT,icon_name)
            with open(icon_path,'ab') as fp:
                for part in icon.chunks():
                    fp.write(part)
                    fp.flush()
            fp.close()

            #将图片路径存入数据库

            user.icon = '/upload/' + icon_name




        user.save()


        #注册成功后,自动登录跳转到首页
        request.session['userid'] = user.id
        return redirect(reverse('AXF:mine'))

    return render(request,'user/register.html')



#登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(name=username,pwd=password)
        if users.exists():
            request.session['userid'] = users.first().id
            return redirect(reverse('AXF:mine'))
        else:
            data = {
                'msg':'用户名密码不匹配,请重新输入'
            }
            return render(request,'user/login.html',data)
    return render(request,'user/login.html')




# 注销
def logout(request):
    del request.session['userid']
    request.session.flush()

    return redirect(reverse('AXF:mine'))



# 加入购物车
def cart_add(request):
    data = {
        'status':1,
        'msg':'success',
    }
    userid = request.session.get('userid',0)
    if not userid:
        data['status'] = 0
        data['msg'] = '您还没登录，请先登录！'
    else:
        # 用户已登录
        if request.method == "GET":
            goodsid = request.GET.get('goodsid')
            num = request.GET.get('num')
            #判断购物车是否已经存在该商品
            carts = Cart.objects.filter(goods_id=goodsid,user_id=userid)
            if carts.exists():
                cart = carts.first()
                cart.num = cart.num + int(num)
                cart.save()
            else:
                # 加入购物车
                cart = Cart()
                cart.user_id = userid
                cart.goods_id = goodsid
                cart.num = num
                cart.save()
        else:
            data['status'] = -1
            data['msg'] = '请求方式错误!'
    return JsonResponse(data)



# 购物车商品数量增加
def cart_num_add(request):
    data = {
        'status':1,
        'msg':'success',
    }
    userid = request.session.get('userid',0)
    if not userid:
        data['status'] = 0
        data['msg'] = '用户未登录，请先登录！'
    else:
        if request.method == "POST":
            cartid = request.POST.get('cartid')
            carts = Cart.objects.filter(id=cartid)
            if carts.exists():
                cart = carts.first()
                cart.num = cart.num + 1
                cart.save()
                #修改成功后，返回最新的商品数量
                data['num'] = cart.num
            else:
                data['status'] = -1
                data['msg'] = '当前商品不存在！'

        else:
            data['status'] = -2
            data['msg'] = 'request method error!'
    return JsonResponse(data)



# 购物车商品数量减少
def cart_num_reduce(request):
    data = {
        'status':1,
        'msg':'success',
    }
    userid = request.session.get('userid',0)
    if not userid:
        data['status'] = 0
        data['msg'] = '用户未登录，请先登录！'
    else:
        if request.method == "POST":
            cartid = request.POST.get('cartid')
            carts = Cart.objects.filter(id=cartid)
            if carts.exists():
                cart = carts.first()
                if cart.num > 1:
                    cart.num = cart.num - 1
                cart.save()
                #修改成功后，返回最新的商品数量
                data['num'] = cart.num
            else:
                data['status'] = -1
                data['msg'] = '当前商品不存在！'

        else:
            data['status'] = -2
            data['msg'] = 'request method error!'
    return JsonResponse(data)


# 购物车商品删除
def cart_goods_del(request):
    data = {
        'status':1,
        'msg':'success',
    }
    userid = request.session.get('userid',0)
    if not userid:
        data['status'] = 0
        data['msg'] = '用户未登录，请先登录！'
    else:
        if request.method == "POST":
            cartid = request.POST.get('cartid')
            carts = Cart.objects.filter(id=cartid)
            if carts.exists():
                cart = carts.first().delete()
            else:
                data['status'] = -1
                data['msg'] = '当前商品不存在！'

        else:
            data['status'] = -2
            data['msg'] = 'request method error!'
    return JsonResponse(data)


# 选中状态
def select_status(request):
    data = {
        'status': 1,
        'msg': 'success',
    }
    userid = request.session.get('userid', 0)
    if not userid:
        data['status'] = 0
        data['msg'] = '用户未登录，请先登录！'
    else:
        if request.method == "POST":

            cartid = request.POST.get('cartid')

            span_status = request.POST.get('span_status')

            # print(cartid,span_status)
            carts = Cart.objects.filter(id=cartid)
            if carts.exists():
                cart = carts.first()
                if span_status:
                    cart.is_select = True
                else:
                    cart.is_select = False
                cart.save()
                data['select_status'] = cart.is_select

                print(data['select_status'])
            else:
                data['status'] = -1
                data['msg'] = '当前商品不存在！'

        else:
            data['status'] = -2
            data['msg'] = 'request method error!'
    return JsonResponse(data)

# 全选/全不选
def cart_select_all(request):
    data = {
        'status': 1,
        'msg': 'success',
    }
    userid = request.session.get('userid', 0)
    if not userid:
        data['status'] = 0
        data['msg'] = '用户未登录，请先登录！'
    else:
        if request.method == "POST":
            is_all_select = int(request.POST.get('isAllSelect'))
            Cart.objects.filter(user_id=userid).update(is_select = not is_all_select)
            data['selectall'] = not is_all_select
        else:
            data['status'] = -2
            data['msg'] = 'request method error!'

    return JsonResponse(data)


#生成随机的图片名
def generate_icon():
    uid = str(uuid.uuid4())
    return my_md5(uid)


def my_md5(string):
    m = hashlib.md5()
    m.update(string.encode())
    return m.hexdigest()