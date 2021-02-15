from flask import Flask

app = Flask(__name__)


@app.route('/')
def im_alive():
    return 'Im Flask and I am barely alive!'
