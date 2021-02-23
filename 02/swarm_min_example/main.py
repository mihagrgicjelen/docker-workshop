from flask import Flask
import os
import time
import requests

app = Flask(__name__)


ip = requests.get('https://wtfismyip.com/json')\
    .json()['YourFuckingIPAddress']


@app.route('/')
def im_alive():

    task_slot = os.environ.get('TASK_SLOT')
    task_name = os.environ.get('TASK_NAME')
    service_name = os.environ.get('SERVICE_NAME')
    node_id = os.environ.get('NODE_ID')

    return \
        'Im Swarmed Flask and I am healthy!<br/>'\
        f'task_slot is: <b>{task_slot}</b><br/>'\
        f'task_name is: <b>{task_name}</b><br/>'\
        f'service_name is: <b>{service_name}</b><br/>'\
        f'node_id is: <b>{node_id}</b><br/>'\
        f'pub IP is: <b>{ip}</b><br/>'
