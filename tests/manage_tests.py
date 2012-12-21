import unittest
from application import app


class ManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def t_username(self, username):
        return self.app.get('/hello/%s' % (username), follow_redirects=True)

    def test_username(self):
        rv = self.t_username('alberto')
        assert "Hello alberto" in rv.data

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'hi' in rv.data
