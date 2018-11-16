from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
import math

def index(request,page):
    show_num = 3
    start = (int(page)-1)*show_num
    end = start + show_num
    obj = Person.objects.all()
    page_count = math.ceil(obj.count()/show_num)
    print(obj.count())
    page_list = [i+1 for i in range(page_count)]
    print(obj[start:end])
    print(page_list)
    cur_page = int(page)
    before_page = cur_page - 1
    next_page = cur_page + 1
    if next_page > page_count:
        next_page = 1
    elif before_page < 1:
        before_page = page_count


    print(cur_page)
    data = {
        'page_list':page_list,
        'page_content':obj[start:end],
        'cur_page':cur_page,
        'before_page':before_page,
        'next_page':next_page
    }

    return render(request,'index.html',data)


def test(request):
    return HttpResponse('abc')