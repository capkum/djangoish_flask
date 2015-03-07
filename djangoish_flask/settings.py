from djangoish_flask import app
import jinja2
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'SECRET_KEY'

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))

# Debug toolbar
DEBUG_TB_ENABLED = True
DEBUG_TB_HOSTS = ('127.0.0.1',)
DEBUG_TB_INTERCEPT_REDIRECTS = False

app.jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('templates'),
])