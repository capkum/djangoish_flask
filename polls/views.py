from djangoish_flask import app, db
from flask import abort, redirect, render_template, request, url_for
from polls import models
from werkzeug.exceptions import BadRequest


@app.route('/polls')
def index():
    latest_question_list = models.Question.query.order_by(models.Question.pub_date.desc())[:5]
    return render_template('polls/index.html', latest_question_list=latest_question_list)


@app.route('/polls/<question_id>')
def detail(question_id):
    question = models.Question.query.get(question_id) or abort(404)
    return render_template('polls/detail.html', question=question)


@app.route('/polls/<question_id>/vote', methods=['POST'])
def vote(question_id):
    question = models.Question.query.get(question_id) or abort(404)
    try:
        selected_choice = question.choice_set.filter_by(id=request.form['choice']).first()
        if not selected_choice:
            raise BadRequest()
    except BadRequest:
        return render_template('polls/detail.html', question=question, error_message="You didn't select a choice.")

    selected_choice.votes += 1
    db.session.add(selected_choice)
    db.session.commit()

    return redirect(url_for('result', question_id=question_id))


@app.route('/polls/<question_id>/result')
def result(question_id):
    question = models.Question.query.get(question_id) or abort(404)
    return render_template('polls/result.html', question=question)