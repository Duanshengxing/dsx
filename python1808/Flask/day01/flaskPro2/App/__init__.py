from flask import Flask
import os
from App.views import blue
def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.path.curdir
    app.register_blueprint(blue)
    return app