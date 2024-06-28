from flask import Flask, jsonify, request
from stardata import data
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        'data': data,
        'message': 'success',
    })

@app.route("/star")
def star():
    star = request.args.get('name')
    star_data = next(item for item in data if item ['name'] == star)
    return jsonify({
        'data': star_data,
        'message': 'success',
    })

app.run(debug = True)
