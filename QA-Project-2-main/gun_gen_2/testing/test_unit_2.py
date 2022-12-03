from flask import url_for
from flask_testing import TestCase

from app import app, gun

class Test_gun_gen_2(TestCase):
    def create_app(self):
        return app

class Test_2(Test_gun_gen_2):
    def test_get_gun(self):
        response = self.client.get(url_for('get_gun'))
        self.assertIn(response.json, gun)
        
class Test_3(Test_gun_gen_2):
    def test_get_gun_2(self):
        response = self.client.get(url_for('get_gun'))
        self.assertEqual(response.status_code, 200)