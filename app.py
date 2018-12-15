# -*- coding: utf-8 -*-

import os
import json
import random
import itertools

from flask import Flask, request, jsonify, render_template

wd = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=os.path.join(wd, 'static'))

with open(os.path.join(wd, 'x.json')) as fin:
    moc = json.load(fin)


la_range = [35.6058333333333, 35.6566666666667]
lo_range = [138.39, 138.46625]
sz = 500
la_coords = [
    la_range[0] + ((la_range[1] - la_range[0]) / sz) * i for i in range(sz)
]
lo_coords = [
    lo_range[0] + ((lo_range[1] - lo_range[0]) / sz) * i for i in range(sz)
]


@app.route("/")
def hello():
    return render_template(os.path.join(wd, 'static/index.html'))


@app.route('/api/<int:datestr>')
def api_datestr(datestr):

    return jsonify([{
        'latitude': x,
        'longitude': y,
        'value': random.uniform(0.0, 0.1)
    } for x, y in itertools.product(la_coords, lo_coords)])


if __name__ == '__main__':
    app.run(debug=True)
