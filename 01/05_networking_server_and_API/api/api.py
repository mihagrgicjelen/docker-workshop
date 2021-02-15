from flask import Flask
import random
import json

app = Flask(__name__)


USERS = [
    {
        'first_name':   'Darth',
        'last_name':    'Vader',
        'email':        'darth_vader@the_empire.com',
    }, {
        'first_name':   'Darth',
        'last_name':    'Maul',
        'email':        'darth_maul@the_empire.com',
    },    {
        'first_name':   'Darth',
        'last_name':    'Vagabondus',
        'email':        'darth_vagabondus@the_empire.com',
    },
]

@app.route('/')
def get_user():
    selected_user = random.choice(USERS)
    return json.dumps(selected_user, indent=4)
