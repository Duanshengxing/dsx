from flask import Flask,render_template
from flask_script import Manager

app = Flask(__name__)
manage = Manager(app)




@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/index/')
def index():
    return 'index!'


if __name__ == '__main__':
    # app.run(host='10.20.158.28',debug=True,port='8000')
    manage.run()