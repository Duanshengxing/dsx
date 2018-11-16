from flask_restful import Resource, fields, marshal_with, reqparse
from App.models import User
from werkzeug.security import check_password_hash


# 参数解析
parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="必须上传用户名")
parser.add_argument("password", type=str, required=True, help="必须上传密码")


# 处理响应数据
user_fields = {
    "u_name": fields.String(attribute="username"),
    "u_email": fields.String(attribute="email"),
    "u_token": fields.String(attribute="user_token"),
}
result_fields = {
    "msg": fields.String,
    "data": fields.Nested(user_fields)
}

# 登录
class LoginResource(Resource):

    @marshal_with(result_fields)
    def post(self):

        # 获取前端参数
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')

        # 登录
        users = User.query.filter(User.username==username)
        if users.count() > 0:
            user = users.first()
            passwd = user.password  # 数据库中加密的密码

            # 检测两个密码是否匹配
            if check_password_hash(passwd, password):
                # 是否激活
                if user.is_active:
                    return {"msg": "登录成功", "data": user}
                else:
                    return {"msg": "未激活，请先激活！"}

            else:
                return {"mgs": "密码错误！"}

        else:
            return {"msg": "用户名不存在"}

