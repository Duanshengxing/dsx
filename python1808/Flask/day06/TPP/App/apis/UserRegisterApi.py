import uuid

from flask import render_template
from flask_mail import Message
from flask_restful import Resource, fields, marshal_with, reqparse

from App.exts import db, mail, cache
from App.models import User

from werkzeug.security import generate_password_hash


# 将前端提交过来的参数进行解析
parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help='必须填写用户名')
parser.add_argument("password", type=str, required=True, help='必须填写密码')
parser.add_argument("email", type=str, required=True, help='必须填写邮箱')


#
user_fields = {
    "u_name": fields.String(attribute="username"),
    "u_email": fields.String(attribute="email"),
    "u_token": fields.String(attribute="user_token"),
}

result_fields = {
    "returnCode": fields.String,
    "msg": fields.String,
    "returnValue": fields.Nested(user_fields)
}

# 注册
class RegisterResource(Resource):

    @marshal_with(result_fields)
    def post(self):
        # 获取前端提交的参数
        args = parser.parse_args()
        username = args.get("username")
        password = args.get("password")
        email = args.get("email")

        # 注册（添加用户数据）
        user = User()
        user.username = username
        user.password = generate_password_hash(password)
        # print(user.password)
        # print(len(user.password))
        user.email = email
        user.user_token = str(uuid.uuid4())  # token, 唯一标识

        try:
            db.session.add(user)
            db.session.commit()

            # 发生邮件激活用户
            # 创建邮件
            msg = Message(subject="淘票票用户激活", sender="niejeff@163.com", recipients=[email])
            # 邮件内容
            # msg.html = "<b>hello 淘票票</b>"
            msg.html = render_template('user_active.html',
                                       username=username,
                                       active_url="http://10.20.158.28:5000/useractive/?token=%s" % user.user_token)
            # 发送邮件
            mail.send(msg)

            # 使用缓存cache
            # 给每个用户单独使用缓存，在5分钟内激活才有效
            cache.set(user.user_token, user.id, timeout=300)


        except Exception as e:
            return {"returnCode": "-1", "msg": str(e)}

        return {"returnCode": "0", "msg": "success", "returnValue": user}

