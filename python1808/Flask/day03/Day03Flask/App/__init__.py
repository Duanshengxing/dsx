from flask import Flask
from .views import init_blue
from .exts import init_all

def init_app():
    app = Flask(__name__)

    DB_URI= 'mysql+pymysql://root:jy1314521@localhost:3306/flaskdb'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_blue(app)
    init_all(app)

    return app