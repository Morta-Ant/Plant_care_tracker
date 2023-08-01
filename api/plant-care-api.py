from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# plant care data
with open("api/plantcare.json") as plants_care:
    plants_care_data = json.load(plants_care)


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
    return jsonify(plants_care_data)


# API Route for a single plant data based on the id
@app.route('/api/plants/<int:id>', methods=["GET"])
def get_plant_by_id(id):
    plant = search_plant_id(id, plants_care_data)
    return jsonify(plant)


# API Route for a single plant data based on the plant name
@app.route('/api/plants/<string:plant_name>', methods=["GET"])
def get_plant_by_name(plant_name):
    plant = search_plant_name(plant_name, plants_care_data)
    return jsonify(plant)


# function to search the plant based on the plant id
def search_plant_id(id, plants_care_data):
    for plant in plants_care_data:
        if plant["_id"] == id:
            return plant
    return None


# function to search the plant based on the plant name
def search_plant_name(plant_name, plants_care_data):
    for plant in plants_care_data:
        if plant["common_name"].lower() == plant_name.lower():
            return plant
    return None


if __name__ == '__main__':
    app.run(port=3000, debug=True)
