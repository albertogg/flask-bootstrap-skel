from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

# Create the app and configuration
# Read the configuration file
app = Flask(__name__)
app.config.from_object('application.default_settings')
app.config.from_envvar('PRODUCTION_SETTINGS', silent=True)

# Connect to database with sqlalchemy.
db = SQLAlchemy(app)


# 404 page not found "route"
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


import application.manager
