from app import create_app, db, cli
from app.models import User, Post, Notification, Message

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, "Message": Message,
    'Notification':Notification}


# to serve, export FLASK_APP=microblog.py
# then flask run
# or use python-dotenv to write down Environ Var.
