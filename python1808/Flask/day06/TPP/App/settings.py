# 配置数据库
# sqlite
# DB_URI = "sqlite:///sqlite3.db"
# mysql
# DB_URI = "mysql+pymysql://root:root@127.0.0.1:3306/db"
#
# # 配置数据库
# app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
# # 禁止对象追踪修改
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


import os

# BASE_DIR: 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#
def db_uri(database):
    db = database.get('DB')
    driver = database.get('DRIVER')
    user = database.get('USER')
    password = database.get('PASSWORD')
    host = database.get('HOST')
    port = database.get('PORT')
    name = database.get('NAME')

    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)

# 配置
class Config(object):
    DEBUG = False

    # 禁止对象追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '111'
    JSON_AS_ASCII = False
    RESTFUL_JSON = dict(ensure_ascii=False)
    # 邮箱配置
    MAIL_SERVER = 'smtp.163.com'  # 163发送邮件的服务器
    MAIL_USERNAME = 'niejeff@163.com'  # 邮箱用户名
    MAIL_PASSWORD = '123456abcde'  # 授权码


# 开发环境
class DevelopConfig(Config):
    # 开启调试模式
    DEBUG = True
    ENV = 'delevelopment'
    TESTING = True
    # 数据库配置
    DATABASE = {
        'DB': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'jy1314521',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'tppdb',
    }
    SQLALCHEMY_DATABASE_URI = db_uri(DATABASE)


# 生产环境
class ProductConfig(Config):
    # 关闭调试模式
    DEBUG = False
    ENV = 'production'
    TESTING = True

    # 数据库配置
    DATABASE = {
        'DB': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': 'jy1314521',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'tppdb',
    }
    SQLALCHEMY_DATABASE_URI = db_uri(DATABASE)


env = {
    'development': DevelopConfig,  # 开发环境
    'production': ProductConfig,  # 生产环境
}











