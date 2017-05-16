

from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from albionmarket_backend import create_app, commands

app = create_app()
manager = Manager(app)


manager.add_command('runserver', Server('0.0.0.0', port=8000))
manager.add_command('db', MigrateCommand)
manager.add_command('drop_db', commands.DropDB)
manager.add_command('seed_data', commands.SeedData)

if __name__ == '__main__':
    manager.run()
