from fabric.api import *


# start with the default server
def run():
    """ Start with the default server """
    local('python runserver.py')


# start with unicorn server.
def grun():
    """ Start with gunicorn server """
    local('gunicorn -c gunicorn.conf runserver:app')


# run tests
def tests():
    """ Run unittests """
    local('python runtests.py --verbose')


# start iteractive shell within the flask environment
def shell():
    """ Start interactive shell within flask environment """
    local('python shell.py')
