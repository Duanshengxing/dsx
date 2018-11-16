from flask_restful import Resource, reqparse, abort
from App.models import User

parser = reqparse.RequestParser()
parser.add_argument("token",type=str,required = True,help="未知用户")

def check_permission(permission):
    def outer(fn):
        def inner(*args,**kwargs):


            _args = parser.parse_args()
            token = _args.get("token")
            print(token)
            users = User.query.filter_by(user_token=token)
            if users.count() > 0:
                user = users.first()
                user_permission = user.permission

                # 判断用户是否有权限使用当前功能
                if permission & user_permission == permission:
                    # 如果有权限则使用功能
                    return fn(*args,**kwargs)
                else:
                    abort(403,message="权限不足")
            else:
                abort(403, message="请先登录")

        return inner
    return outer




class PermissionResource(Resource):
    @check_permission(4)
    def get(self):
        return {"msg":"可以免广告"}

    @check_permission(8)
    def post(self):
        return {"msg":"可以免流量"}



