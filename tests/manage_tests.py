import os
import unittest
from application.default_settings import _basedir
from application import app, db


class ManagerTestCase(unittest.TestCase):
    """ setup and teardown for the testing database """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:////'
                                    + os.path.join(_basedir, 'db/tests.db'))
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class OriginalRoutes(ManagerTestCase):
    """ test suite for the original in app routes """

    def route_username(self, username):
        return self.app.get('/hello/%s' % (username), follow_redirects=True)

    def test_username(self):
        rv = self.route_username('alberto')
        assert "Hello, alberto" in rv.data

    def test_index(self):
        rv = self.app.get('/')
        assert 'hi' in rv.data
