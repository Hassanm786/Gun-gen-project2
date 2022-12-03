from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app
import application.routes


class TestHome(TestCase):
    def create_app(self):
        return app


    def test_home_page(self):
        gun = 'Rifle'
        perk_one = 'Faster Reload'
        perk_two = 'increased damage against undead'
        gun_effect = 'Fire Damage'
        result = f"You have created a {gun} with the following perks: {perk_one} and {perk_two} and the gun effect of: {gun_effect}"

        with requests_mock.Mocker() as m:
            m.get('http://gun_gen_2:5000/get_gun', json={'gun': gun})
            m.get('http://perk_one_3:5000/get_perk1', json={'perk_one': perk_one})
            m.post('http://perk_two_4:5000/get_perk2', json={'gun': gun, 'perk_one': perk_one, 'perk_two': perk_two, 'gun_effect': gun_effect})
            response = self.client.get(url_for('home'))