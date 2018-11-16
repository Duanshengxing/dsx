from random import *

from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image,ImageFont,ImageDraw
import os
import io
# Create your views here.
from Day08Django.settings import BASE_DIR


def index(request):
    if request.method == "POST":
        code = request.POST.get('check')
        verify_code = request.session.get('verify_code')
        if code == verify_code:
            return HttpResponse('验证成功！')
        else:
            return HttpResponse('验证失败！')
    else:

        return render(request,'MiddleApp/index.html')

def generate_verify(request):
    size = (100,50)
    bgcolor = random_color()
    image = Image.new("RGB",size,bgcolor)

    path = os.path.join(BASE_DIR, r'static/fonts/ADOBEARABIC-BOLD.OTF')
    string = "0123456789abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(path)
    draw = ImageDraw.Draw(image)
    verify_code = ''
    for i in range(4):
        font = string[randrange(len(string))]
        font_color = random_color()
        verify_code += font
        font_style = ImageFont.truetype(path,randint(27,35))
        draw.text((10+i*20,randint(5,15)),font,font=font_style,fill=font_color)

    request.session['verify_code'] = verify_code
    for i in range(300):
        draw.point((randint(1,99),randint(1,49)),fill=random_color())


    buf = io.BytesIO()
    image.save(buf,'png')
    return HttpResponse(buf.getvalue(),'image/png')



def random_color():
    return randint(0,255),randint(0,255),randint(0,255)