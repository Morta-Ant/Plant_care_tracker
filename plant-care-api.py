from flask import Flask, jsonify, request
import json
from database.crud_plants import get_all_plants, get_plant_by_id, get_plant_by_name

app = Flask(__name__)

# Route
@app.route('/')
def hello():
    return jsonify({
        'hello': 'Plant lovers',
        'goodbye': 'Dying plants'
    })


# API Route for all plants data
@app.route('/api/plants', methods=["GET"])
def get_plants():
    return jsonify(get_all_plants())


# API Route for a single plant data based on the id
@app.route('/api/plants/<int:id>', methods=["GET"])
def get_plant_by_id(id):
    return jsonify(get_plant_by_id(id))


# API Route for a single plant data based on the plant name
@app.route('/api/plants/<string:plant_name>', methods=["GET"])
def get_plant_by_name(plant_name):
    return jsonify(get_plant_by_name(plant_name))


if __name__ == '__main__':
    app.run(port=3000, debug=True)
