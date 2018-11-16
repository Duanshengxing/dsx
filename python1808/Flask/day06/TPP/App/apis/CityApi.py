from App.models import *
from flask_restful import Resource, fields, marshal_with, reqparse, marshal



# 处理返回字段
city_fields = {
    "id": fields.Integer,
    "parentId": fields.Integer,
    "regionName": fields.String,
    "cityCode": fields.Integer,
    "pinYin": fields.String
}

letter_fields = {
    "A": fields.List(fields.Nested(city_fields)),
    "B": fields.List(fields.Nested(city_fields)),
    "C": fields.List(fields.Nested(city_fields)),
    "D": fields.List(fields.Nested(city_fields)),
    "E": fields.List(fields.Nested(city_fields)),
    "F": fields.List(fields.Nested(city_fields)),
    "G": fields.List(fields.Nested(city_fields)),
    "H": fields.List(fields.Nested(city_fields)),
}

result_fields = {
    "returnCode": fields.String,
    "returnValue": fields.Nested(letter_fields)
}

# 城市数据api
class CityResource(Resource):

    @marshal_with(result_fields)
    def get(self):

        # 获取所有城市数据
        city_letters = CityLetter.query.all()

        return_value = {}

        for city_letter in city_letters:
            citys = city_letter.citys  # 每个字母包含的所有城市列表
            return_value[city_letter.letter] = citys


        data = {
            "returnCode": "0",
            "returnValue": return_value,
        }
        return data


    # 不适用marshal_with
    def post(self):
        # 获取所有城市数据
        city_letters = CityLetter.query.all()

        return_value = {}
        letter_fields_dynamic = {}

        for city_letter in city_letters:
            citys = city_letter.citys  # 每个字母包含的所有城市列表
            return_value[city_letter.letter] = citys

            letter_fields_dynamic[city_letter.letter] = fields.List(fields.Nested(city_fields))

        # print(letter_fields_dynamic)

        result_fields_dynamic = {
            "returnCode": fields.String,
            "returnValue": fields.Nested(letter_fields_dynamic)
        }

        data = {
            "returnCode": "0",
            "returnValue": return_value,
        }
        return marshal(data, result_fields_dynamic)


'''
{
  "returnCode": "0",
  "returnValue": {
    "A": [
      {
        "id": 3643,
        "parentId": 0,
        "regionName": "阿坝",
        "cityCode": 513200,
        "pinYin": "ABA"
      },
      ...
    ]
    "B": [
      {},
      {}
    ]
}
'''









