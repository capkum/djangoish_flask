# djangoish_flask
A flask skeleton project to help django developers understand flask.

![](http://i.imgur.com/GV04zF3.png)
## Getting started
Clone this repository:
```
$ git clone https://github.com/ironyee/djangoish_flask.git
```
Use the requirements.txt to install pip packages in your virtualenv:
```
$ pip install -r requirements.txt
```
Initialize database:
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
Run server:
```
$ python manage.py runserver [-h 127.0.0.1] [-p 5000]
```
* Poll app: [http://127.0.0.1:5000/polls/](http://127.0.0.1:5000/polls/)
* Admin page: [http://127.0.0.1:5000/admin/](http://127.0.0.1:5000/admin/)

## Dependencies
* Flask
* Flask-Admin
* Flask-DebugToolbar
* Flask-Migrate (Alembic wrapper for flask)
* Flask-SQLAlchemy
