from flask import Blueprint, render_template

blue = Blueprint('blue',__name__)

def init_blue(app):
    app.register_blueprint(blue)

@blue.route("/index/")
def index():
    return render_template('index.html')

@blue.route("/movie_list/")
def movie_list():
    return render_template("movies.html")
