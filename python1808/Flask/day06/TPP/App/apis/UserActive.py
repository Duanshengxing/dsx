from flask_restful import fields, Resource, marshal_with, reqparse

from App.exts import db, cache
from App.models import User

# 参数解析
parser = reqparse.RequestParser()
parser.add_argument("token", type=str, required=True, help='未知用户')


# 用户激活
class UserActiveResource(Resource):

    def get(self):
        args = parser.parse_args()
        token = args.get("token")

        # 获取对应用户的缓存，如果存在则可以激活，如果不存在则说明已经超过5分钟
        userid = cache.get(token)

        # 如果有缓存，则激活
        if userid:

            # 修改token对应用户的激活状态
            users = User.query.filter_by(user_token=token)
            if users.count() > 0:
                user = users.first()
                user.is_active = True  # 将激活状态改为True(已激活)
                db.session.commit()

                # 删除缓存cache
                cache.delete(token)

                return {"msg": "success,激活成功!"}

            else:
                return {"msg": "fail,用户不存在，无法激活!"}
        # 如果没有缓存，则不可以激活
        else:
            return {"msg": "fail,已过期，激活失败!"}
