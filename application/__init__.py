from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#configuration file
app = Flask(__name__)
app.config.from_object('application.default_settings')
app.config.from_envvar('PRODUCTION_SETTINGS', silent=True)

# connect to database.
db = SQLAlchemy(app)

import application.manager