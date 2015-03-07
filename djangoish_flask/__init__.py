from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.admin import Admin
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from jinja2_pluralize import pluralize_dj

app = Flask(__name__)
app.config.from_object('djangoish_flask.settings')

# Admin
admin = Admin(app)

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Debug toolbar
toolbar = DebugToolbarExtension(app)

# Register template filter
app.template_filter('pluralize')(pluralize_dj)

# admin/model/view
from polls import admin
from polls import models
from polls import views