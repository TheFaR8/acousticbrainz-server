from __future__ import absolute_import
from web_server.testing import ServerTestCase
from flask import url_for


class LoginViewsTestCase(ServerTestCase):

    def test_login_page(self):
        response = self.client.get(url_for('login.index'))
        self.assert200(response)
