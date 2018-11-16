from flask import Blueprint, render_template

blue = Blueprint('blue',__name__)

@blue.route('/index/')
def index():
    return render_template('index.html')
