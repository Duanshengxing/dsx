from App import init_app
from flask_script import Manager


app = init_app()
manage = Manager(app)

if __name__ == '__main__':
    manage.run()
