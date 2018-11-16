from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'publisher/index.html')


def detail(request,author_id):
    author = Author.objects.get(id=author_id)
    return  render(request,'author/detail.html',{'author':author})