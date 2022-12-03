from application import app
from flask import render_template, redirect, url_for, request
import requests, json



@app.route('/home', methods=["GET", "POST"])
def home():
    gun = requests.get('http://gun_gen_2:5000/get_gun').json()
    perk_one = requests.get('http://perk_one_3:5000/get_perk1').json()

    generate = {'gun': gun, 'perk_one': perk_one}

    gun_mod = requests.post('http://perk_two_4:5000/get_perk2', json=generate).json()

    # new_gun = gun=gun_mod['gun'], perk_one=gun_mod['perk_one'], perk_two=gun_mod['perk_two'], gun_effect=gun_mod['gun_effect']

    result = f"You have created a {gun_mod['gun']} with the following perks: {gun_mod['perk_one']} and {gun_mod['perk_two']} and the gun effect of: {gun_mod['gun_effect']}"

    return render_template('main.html', result=result)



