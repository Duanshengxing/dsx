

# json解析： json字符串 => json对象（如：Python字典,列表） json.load(fp), json.loads(string)
# json序列化： json对象 => json字符串  json.dump(fp), json.dumps(string)

import json

# JSON字符串
#  "hello" 是JSON字符串
#  '[]': 是
#  '{}'：是
#  '{"like": ['code', 'movie']}' : 是
#  "{'name': 'lisi'}" : 不是
#  '{"name"' : 不是

# json解析： json字符串 => json对象（如：Python字典,列表） json.load(fp), json.loads(string)
json_str = '{"name":"lisi", "likes": ["movie", "code"]}'
json_obj = json.loads(json_str)
print(json_obj)  # {'name:': 'lisi', 'likes': ['movie', 'code']}
print(type(json_obj))  # <class 'dict'>

json_obj = {'name:': 'lisi', 'likes': ['movie', 'code']}
json_str = json.dumps(json_obj)
print(json_str)  # '{"name:": "lisi", "likes": ["movie", "code"]}'
print(type(json_str))  # <class 'str'>

# json.load(fp)
# json.dump(obj, fp)


# JS :
#   JSON.parse()： 解析
#   JSON.stringify() : 序列化


