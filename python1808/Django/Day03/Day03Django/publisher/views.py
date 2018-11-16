from django.shortcuts import render

# Create your views here.
from publisher.models import Publisher


def index(request):
    return render(request, 'publisher/index.html')

def detail(request,publisher_id):
    publisher = Publisher.objects.get(id=publisher_id)
    return  render(request,'publisher/detail.html',{'publisher':publisher})