from datetime import datetime
from djangoish_flask import db


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    choice_set = db.relationship('Choice', backref='question', cascade='all', lazy='dynamic')

    def __str__(self):
        return self.question_text


class Choice(db.Model):
    __tablename__ = 'choice'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_text = db.Column(db.String(200), nullable=False)
    votes = db.Column(db.Integer(), nullable=False, default=lambda: 0)

    def __str__(self):
        return self.choice_text