import pymysql
import json

# json解析： json字符串 => json对象（如：Python字典,列表） json.load(fp), json.loads(string)
# json序列化： json对象 => json字符串  json.dump(fp), json.dumps(string)


# 获取json城市数据并加入数据库中
def city_data():

    # 连接数据库
    db = pymysql.Connect(host='localhost', port=3306, user='root', password='jy1314521', database='tppdb', charset='utf8')
    cursor = db.cursor()

    # 获取json数据并插入数据库
    with open('citys.json', encoding='GBK') as fp:
        # json.load(fp)
        # json.loads(fp.read())
        content_dict = json.load(fp)  # 获取json文件中的字典数据
        # print(type(content_dict))  # <class 'dict'>

        # 获取所有城市数据
        return_value = content_dict.get("returnValue")

        # 获取所有城市字母
        city_letters = return_value.keys()

        # 开始事务
        db.begin()

        # 遍历所有城市字母
        for key in city_letters:
            # 插入城市字母数据到数据库表city_letter中
            # cursor.execute("insert into city_letter(letter) values('%s')" % key)

            # 获取每个字母分类下的所有城市
            citys = return_value.get(key)

            # 遍历所有城市
            for city in citys:
                id = city.get('id')
                parentId = city.get('parentId')
                regionName = city.get('regionName')
                cityCode = city.get('cityCode')
                pinYin = city.get('pinYin')

                # 获取字母数据对应的id
                cursor.execute("select id from city_letter where letter='%s'" % key)
                res = cursor.fetchone()
                # print(res)  # (32,)
                letter_id = res[0]

                # 插入城市数据
                cursor.execute('insert into city(id,parentId,regionName,cityCode,pinYin,letter_id) '
                               'values(%d, %d, "%s", %d, "%s", %d)'
                               % (id, parentId, regionName, cityCode, pinYin, letter_id))


        # 提交事务
        db.commit()


    # 关闭数据库连接
    cursor.close()
    db.close()



if __name__ == "__main__":
    city_data()







