from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return "hello back!"


@app.route('/data')
def data():
    data = {"names": ["A", "B", "C", "D"]}
    return jsonify(data)


from app.routes import *