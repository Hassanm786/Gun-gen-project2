from flask import Flask, jsonify
import random


app = Flask(__name__)

gun = {'Sniper', 'Shotgun', 'Rifle', 'Pistol', 'SMG', 'Assault Rifle', 'LMG', 'Rocket Launcher'}

@app.route('/get_gun')
def get_gun():
    return jsonify(random.choice(list(gun)))


if __name__=='__main__': app.run(host = "0.0.0.0", port = 5000)