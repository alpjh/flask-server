from app import app
from flask import jsonify, request


@app.route('/')
def index():
    return "hello back!"

@app.route('/data')
def data():
    data = {"names": ["A", "B", "C", "D"]}
    return jsonify(data)

