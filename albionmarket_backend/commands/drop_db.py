

from flask_script import prompt_bool, Command

from .. import extensions


class DropDB(Command):
    def run(self):
        if prompt_bool('Are you sure you want to lose all your data!?'):
            extensions.db.drop_all()