from django.shortcuts import render

# Create your views here.
from book.models import Book


def index(request):
    return render(request,'book/index.html')

def list(request):
    book_all = Book.objects.all()
    return render(request,'book/list.html',{'book_all':book_all})

def detail(request,book_title):
    book_info = Book.objects.get(title=book_title)
    return render(request,'book/detail.html',{'book_info':book_info})