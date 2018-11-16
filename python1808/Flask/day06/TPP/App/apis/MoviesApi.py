from App.models import Movies
from flask_restful import Resource,marshal_with,fields,reqparse


# 请求参数解析
parser = reqparse.RequestParser()

parser.add_argument("flag",type=int,default = 1)
#flag:1表示正在热映,2表示即将上映

movie_fields = {
    "id":fields.Integer,
    "showname":fields.String,
    "shownameen": fields.String,
    "director": fields.String,
    "leadingRole": fields.String,
    "type": fields.String,
    "country": fields.String,
    "language": fields.String,
    "duration": fields.Integer,
    "screeningmodel": fields.String,
    "openday": fields.DateTime,
    "backgroundpicture": fields.String,

    # id, showname, shownameen, director, leadingRole, type, country, language, duration, screeningmodel, openday, backgroundpicture, flag, isdelete
}


result_fields = {
    "movies":fields.List(fields.Nested(movie_fields))
}



class MoviesResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        args = parser.parse_args()
        flag = args.get("flag")
        movies = Movies.query.filter_by(flag=flag).limit(10)


        data = {
            "movies":movies
        }
        return data