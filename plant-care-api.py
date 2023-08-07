from flask import Flask, jsonify, request
from database.crud_plants import get_all_plants, get_plant_by_id, get_plant_by_name
from database.crud_plant_collection import get_all_plant_collections, get_plant_collection_by_ids,get_plant_collection_by_user,create_plant_collection,update_plant_collection,delete_plant_collection
from datetime import datetime, timedelta

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
def get_plants_endpoint():
    all_plants = get_all_plants()
    return jsonify(all_plants)


# API Route for a single plant data based on the id
@app.route('/api/plants/<int:id>', methods=["GET"])
def get_plant_by_id_endpoint(id):
    plant_by_id = get_plant_by_id(id)
    return jsonify(plant_by_id)


# API Route for a single plant data based on the plant name
@app.route('/api/plants/<string:plant_name>', methods=["GET"])
def get_plant_by_name_endpoint(plant_name):
    plant_by_name = get_plant_by_name(plant_name)
    return jsonify(plant_by_name)

# API route to add a plant to a collection that links it to the user
@app.route('/api/collection', methods=["POST"])
def add_plant_to_collection_endpoint():
    plant_collection_data = request.get_json()
    required_fields = ['user_id', 'plant_id', 'last_care']
    for field in required_fields:
        if field not in plant_collection_data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    last_care_date = plant_collection_data['last_care']
    plant = get_plant_by_id(plant_collection_data['plant_id'])
    care_frequency = plant['watering_frequency']
    upcoming_care_date = get_next_care_date(last_care_date, care_frequency)
    plant_collection_data['upcoming_care'] = upcoming_care_date
    create_plant_collection(plant_collection_data)
    return jsonify({"message": "Plant collection data added successfully."})

# API route to get plant collection for a specific user

# API route to get a specific plant from plant collection for a specific user

# API route to update last care and upcoming care date for specific plant and specific user

# API route to delete specific plant from plant-collection table for a specific user






def get_next_care_date(last_care_date, care_frequency):
     
     # Convert the last_care_date string to a datetime object
        last_care_datetime = datetime.strptime(last_care_date, '%Y-%m-%d %H:%M:%S')

    # Calculate the upcoming care date by adding care_frequency days to last_care_datetime
        upcoming_care_datetime = last_care_datetime + timedelta(care_frequency)

    # Convert the upcoming_care_datetime back to a formatted string
        next_care_date = upcoming_care_datetime.strftime('%Y-%m-%d %H:%M:%S')

        return next_care_date

if __name__ == '__main__':
    app.run(port=3000, debug=True)
