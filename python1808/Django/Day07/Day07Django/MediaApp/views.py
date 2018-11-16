
from django.shortcuts import *
import uuid,os,hashlib

from Day07Django.settings import MEDTA_ROOT
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def receive(request):
    if request.method == "POST":
        user = request.POST.get('user')
        header = request.FILES.get('pic')
        header_name = generate_icon() + os.path.splitext(header.name)[1]
        path = os.path.join(MEDTA_ROOT,header_name)
        with open(path,'ab') as f:
            for data in header.chunks():
                f.write(data)
                f.flush()

        usermodel = UserModel()
        usermodel.name = user
        usermodel.root = "/upload/"+header_name
        usermodel.save()

        return HttpResponse('上传成功')





















def generate_icon():
    code = str(uuid.uuid4())
    m = hashlib.md5()
    m.update(code.encode())
    return m.hexdigest()

