from djangoish_flask import admin, db
from flask.ext.admin.contrib.sqla import ModelView
from polls import models


class QuestionModelView(ModelView):
    inline_models = (models.Choice,)


admin.add_view(QuestionModelView(models.Question, db.session))
admin.add_view(ModelView(models.Choice, db.session))