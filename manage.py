import os
from app import create_app
from app.modules import User, Content, Category, Comment, Options
from flask.ext.script import Manager, Shell


if os.name == "posix":
    FLASK_CONFIG = "product"
else:
    FLASK_CONFIG = "develop"

app = create_app(FLASK_CONFIG)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, User=User, Content=Content,
                Category=Category, Comment=Comment, Options=Options)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()