from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def check(request):
    flag = 0
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        repwd = request.POST.get('repwd')

        user_pwd = UserModels.objects.filter(user=user,pwd=pwd)
        user_list = UserModels.objects.filter(user = user)

        if repwd:
            if pwd == repwd:
                flag = 1
            elif user_list:
                flag = 2
            else:
                flag = 3
            return render(request,"check.html",{'flag':flag})
        else:
            if user_pwd.exists():
                flag = 4
            else:
                flag = 5
            return render(request, "check.html", {'flag': flag})


