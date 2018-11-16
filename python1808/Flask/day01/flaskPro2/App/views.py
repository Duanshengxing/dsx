import uuid

from flask import Blueprint, redirect, url_for, request, render_template, make_response, Response, abort, session

blue = Blueprint('first',__name__)

@blue.route('/')
def hello():
    return '胡仙仙是儿'

@blue.route('/getstudent/<id>/')
def get_student(id):
    print(id)
    print(type(id))
    return 'get_student:%s' % id

@blue.route('/getperson/<int:id>/')
def get_person(id):
    print(id)
    print(type(id))
    return 'getperson:%d'%id


@blue.route('/getmoney/<float:money>/')
def get_money(money):
    print(money)
    print(type(money))
    return 'getmoney: %.2f' % money


@blue.route('/getpath/<path:p>/')
def get_path(p):
    print(p)
    print(type(p))
    return 'getpath:%s' % p


@blue.route('/getany/<any(movie,music,code):like>/')
def get_any(like):
    print(like)
    print(type(like))
    return 'getany:%s' % like



@blue.route('/getuuid/<uuid:uid>/')
def get_uuid(uid):
    print(uid)
    print(type(uid))
    return 'getuuid:%s' % uid


#反向解析
@blue.route('/redirect/')
def make_redirect():
    # return redirect('http:www.baidu.com')
    return redirect(url_for('first.get_path',p='12/3'))


@blue.route('/request/',methods=['GET','POST'])
def get_request():
    # print(request.url)
    # print(request.base_url)
    # print(request.host_url)
    # print(request.host)
    # print(request.path)



    return 'nishuone'



@blue.route('/response/',methods = ['GET','POST'])
def get_response():
    # response = render_template('index.html',name='范冰冰')
    # response = make_response(render_template('index.html',name='范冰冰'))
    response = Response(render_template('index.html',name='范冰冰'))


    return response


@blue.route('/exception/')
def get_exc():
    abort(400)

    return

@blue.errorhandler(400)
def handle(e):
    print(type(e))
    return '处理404错误成功'



@blue.route('/setcookie/',methods = ['GET','POST'])
def set_cookie():
    response = Response(render_template('index.html',name='范冰冰'))
    response.set_cookie('user','fanbingbing')
    return response




@blue.route('/getcookie/',methods = ['GET','POST'])
def get_cookie():
    user = request.cookies.get('user')
    return user


@blue.route('/deletecookie/',methods = ['GET','POST'])
def delete_cookie():
    response = Response('<b>范冰冰</b>')
    response.delete_cookie('user')
    return response


@blue.route('/setsession/',methods = ['GET','POST'])
def set_session():
    session.clear()
    return 'abc'






# eyJwd2QiOnsiIHUiOiI2YzJmOTRiYTJlMzE0YjI0YWFkZTE5MzFlMTlkMjc4NSJ9fQ.DpzQIw.to9eXfv5V-2ONRtGe90hftf_N0s


