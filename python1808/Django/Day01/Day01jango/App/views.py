from django.shortcuts import render
from datetime import *

# Create your views here.

from django.http import HttpResponse

from App.models import *


def welcome(request):
    return HttpResponse('hello world')


def love(request):
    return render(request, 'love.html')

def grade(request):
    data_list = Grade.objects.all()
    return  render(request,'show_all.html',{'data_list':data_list})

def showtime(request):

    return render(request,'showtime.html')

def show_stu(request):
    data_all = Student.objects.all()
    return render(request,'showall_stu.html',{'data_all':data_all})