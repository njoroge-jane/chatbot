from app import create_app
from app import db
from flask_script import Manager,Server
from app.models import registration,pin,chat, contacts
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')


manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,registration = registration,pin=pin,chat=chat, contacts = contacts)


if __name__ == '__main__':
    app.run()    
    # manager.run()