# -*- coding: utf-8 -*-

import os

from flask import Flask, request, jsonify, render_template

wd = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=os.path.join(wd, 'static'))

@app.route("/")
def hello():
    return render_template(os.path.join(wd, 'static/index.html'))


@app.route('/api/<int:datestr>')
def api_datestr(datestr):
    return jsonify([
        {'latitude': 35.868698, 'longitude': 138.276653}
    ])


if __name__ == '__main__':
    app.run(debug=True)