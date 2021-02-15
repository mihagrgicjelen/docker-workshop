from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def im_alive():
    emails = [
        requests.get('http://api:8888').json(),
        requests.get('http://api:8888').json(),
    ]

    emails_string = '<br/>'.join([x['email'] for x in emails])

    return f'Emails from the empire are: <br/><b>{emails_string}</b>'
