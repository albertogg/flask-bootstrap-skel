from application import app
from flask import render_template
from models import *


@app.route('/')
@app.route('/index')
def hello():
    return render_template('base.html')


@app.route('/hello/<username>')
def hello_username(username):
    return "Hello %s!" % username
