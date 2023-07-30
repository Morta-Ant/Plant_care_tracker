from flask import Flask, jsonify, request
from plant_care_data import plant_data

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
    return jsonify(plant_data)


# API Route for a single plant data based on the id
@app.route('/api/plants/<int:id>', methods=["GET"])
def get_plant_by_id(id):
    plant = search_plant_id(id, plant_data)
    return jsonify(plant)


@app.route('/api/plants/<string:plant_name>', methods=["GET"])
def get_plant_by_name(plant_name):
    plant = search_plant_name(plant_name, plant_data)
    return jsonify(plant)


def search_plant_id(id, plant_data):
    for plant in plant_data:
        if plant["_id"] == id:
            return plant
    return None


def search_plant_name(plant_name, plant_data):
    for plant in plant_data:
        if plant["common_name"].lower() == plant_name.lower():
            return plant
    return None


if __name__ == '__main__':
    app.run(debug=True)
