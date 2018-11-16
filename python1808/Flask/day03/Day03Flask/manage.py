from flask_script import Manager
from App import init_app
from App.exts import db
from flask_migrate import MigrateCommand

app = init_app()
manage = Manager(app)
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()