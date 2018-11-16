from django.shortcuts import render,redirect,reverse

# Create your views here.
from App.models import Student


def index(request):
    stu_all = Student.objects.all()
    return render(request,'index.html',{'stu_all':stu_all})

def detail(request,stu_id):
    stu = Student.objects.get(id = stu_id)
    return  render(request,'detail.html',{'stu':stu})

def detail2(request,id1,id2):
    stu = Student.objects.get(id = id2)
    return render(request,'detail.html',{'stu':stu})

def detail3(request,id2,id1):
    stu = Student.objects.get(id = id2)
    return render(request,'detail.html',{'stu':stu})

def success(request):
    # return render(request,'success.html')
    return redirect(reverse('app:detail3',kwargs={'id1':1,'id2':2}))