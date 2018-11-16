from flask import Flask
from App.urls import *
from App.exts import init_exts
from App.settings import env
from .views import init_blue

# 初始化app
def init_app():
    # 创建flask应用app
    app = Flask(__name__)

    # 添加配置信息
    app.config.from_object(env.get('development'))
    # print(app.config)
    init_blue(app)

    # 初始化插件
    init_exts(app)


    return app


