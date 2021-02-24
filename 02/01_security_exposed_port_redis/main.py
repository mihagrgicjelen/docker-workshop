from flask import Flask
import redis


SECRET_AGENS = [
    ('Darth Vader', 'Ljubljana', '1.1.2021 - 1.3.2021'),
    ('Darth Jaka', 'Maribor', '1.1.2021 - '),
    ('Darth Matija', 'Koper', '2.1.2021 - '),
]

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379, password='empire_is_dark')


@app.route('/')
def im_alive():
    trs = [
        f'<tr><td>{name}<td><td>{place}<td><td>{date_str}<td></tr>'
        for name, place, date_str in SECRET_AGENS
    ]

    visit_count = int(cache.get('visit_count')) \
        if cache.get('visit_count') else 0
    cache.set('visit_count', visit_count + 1)

    return \
        f'<h1>List of our secret agents</h1>'\
        f'<h2 style="color: red">SENSIBLE DATA</h2><br/>'\
        f'<table>{"".join(trs)}</table><br/>'\
        f'Visit count: {visit_count}'
