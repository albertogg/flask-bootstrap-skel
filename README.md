Flask-Bootstrap-Skel
---

Is a skeleton of a "Large" Flask application with Twitter bootstrap integration.

### New project name

Please update the remote URL

~~~sh
$ git remote set-url origin https://github.com/albertogg/flask-bootstrap-skel.git

or 

$ git remote set-url origin git@github.com:albertogg/flask-bootstrap-skel.git
~~~

![Index pic](http://i.imgur.com/1NWEt.png "index")
** index.html **

Code Status
---
[![Build Status](https://travis-ci.org/albertogg/flask-bootstrap.png)](https://travis-ci.org/albertogg/flask-bootstrap)


Requirements
---
* Python 2.7 or 2.6
* Sqlite
* pip

Getting started
---

Clone the repo to your computer in the desired folder:

~~~ sh
$ git clone https://github.com/albertogg/flask-bootstrap-skel.git
~~~

Use the requirements.txt to start dependencies in your virtualenv:

~~~ sh
$ pip install -r requirements.txt
~~~

Start the server:

~~~ sh
$ fab run
or
$ fab grun # for gunicorn server
~~~

Open the browser; `http://localhost:5000` or with the terminal(OS X):

~~~ sh
$ open http://localhost:5000
~~~

Initialize db
---

Set the db parameters in the default_settings.py or in the production.cfg file and start python interactive shell within the flask environment:

~~~ sh
$ fab shell
>>> db.create_all()
>>> exit()
~~~

***note: You must first create the database in Postgresql. From running this command on heroku, you will need to use heroku run "fab shell"***

Unit testing
---

Add unittests to the manage_tests.py file and then start running the tests:

~~~ sh
$ fab tests
~~~

Production Configuration
---

To activate the production configuration; export the variable:

~~~ sh
$ export PRODUCTION_SETTINGS=/path/to/production.py
~~~

***For Heroku using gunicorn and production settings, do the following:***.

**Heroku Postgresql Database** as primary,
Check [heroku](https://devcenter.heroku.com/articles/heroku-postgresql#establish-primary-db).

~~~ sh
$ heroku config:set PYTHONPATH='fakepath'
$ heroku config:add PRODUCTION_SETTINGS='application/production.py'
~~~

Alembic Migrations
---

The flask-bootstrap skeleton now supports migrations using Alembic and Flask-SQLAlchemy. [Auto Generating Migrations](http://alembic.readthedocs.org/en/latest/tutorial.html#auto-generating-migrations) are working!

~~~ sh
$ alembic revision --autogenerate -m "Added users table"
~~~

Contribute
---
1. Fork the repository on Github.
2. Send a pull request and don't forget to add yourself to the AUTHORS.md file.

Changelog
---
**v0.4.1 / 2013/03/07**
  * Alembic Migrations.
  * AUTHORS.md

**v0.4 / 2013/03/07**
  * Heroku ready
  * requirements.
  * Error pages.
  * bootstrap 2.3

**v0.3 / 2013/01/06**
  * Python 2.6 support.
  * Shell script.
  * gunicorn ready.
  * Sqlite ready for dev/testing environment.
  * db directory for Sqlite db's

**v0.2 / 2012/12/28**
  * Add Unittests
  * License
  * Configuration files
  * index.html template

**v0.1 / 2012/12/22**
  * Create Flask-Bootstrap skeleton.
  * Add Twitter bootstrap 2.2.2 to project.
  * Add SQLAlchemy to default skeleton.

ToDo
---
* **Add Flask-Security Support**
* Add support for multiple python versions.
* Add a mock library for testing
* support for many db's.
* More...
