from application import app
from models import *


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/hello/<username>')
def hello_username(username):
    return "Hello %s!" % username
