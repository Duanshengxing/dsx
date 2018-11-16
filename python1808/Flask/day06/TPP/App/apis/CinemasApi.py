from App.models import Cinemas
from flask_restful import Resource,marshal_with,fields,reqparse


# 请求参数解析
parser = reqparse.RequestParser()

parser.add_argument("city",type=str,default = "深证")
parser.add_argument("district",type=str, default="全部区域")
parser.add_argument("sort",type=int,default=1)
#flag:1表示正在热映,2表示即将上映

cinemas_fields = {
    "name":fields.String,
    "city": fields.String,
    "district": fields.String,
    "address": fields.String,
    "phone": fields.String,
    "score": fields.Float,
    "hallnum": fields.Integer,
    "servicecharge": fields.Float,
    "astrict": fields.Integer,

}


result_fields = {
    "cinemas":fields.List(fields.Nested(cinemas_fields))
}



class CinemasResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        args = parser.parse_args()
        city = args.get("city")
        district = args.get("district")
        sort = args.get("sort")
        cinemas = Cinemas.query.filter_by(city = city)
        if district != "全部区域":
            cinemas = cinemas.filter_by(district=district)

        #排序
        if sort == 1:
            pass
        elif sort == 2:
            cinemas = cinemas.order_by("-score")


        data = {
            "cinemas":cinemas,
        }
        return data