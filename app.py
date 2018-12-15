# -*- coding: utf-8 -*-

import os
import json

from flask import Flask, request, jsonify, render_template

wd = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=os.path.join(wd, 'static'))

with open(os.path.join(wd, 'x.json')) as fin:
    moc = json.load(fin)


@app.route("/")
def hello():
    return render_template(os.path.join(wd, 'static/index.html'))


@app.route('/api/<int:datestr>')
def api_datestr(datestr):
    print(moc)
    return jsonify(moc)


if __name__ == '__main__':
    app.run(debug=True)