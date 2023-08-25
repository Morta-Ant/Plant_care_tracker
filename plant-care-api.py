from flask import Flask, jsonify, request
from database.crud_plants import get_all_plants, get_plant_by_id, get_plant_by_name
from database.crud_plant_collection import get_plant_in_collection_by_id ,add_plant_to_collection,update_plant_in_collection,delete_plant_from_collection, get_plants_in_user_collection
from utils.get_next_care_date import get_next_care_date

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

class PlantNotFoundError(Exception):
    def __init__(self, plant_id):
        self.plant_id = plant_id
        self.message = f"Plant with ID {plant_id} has not been found."
        
@app.route('/api/plants/<int:plant_id>', methods=["GET"])
def get_plant_by_id_endpoint(plant_id):
    try:
        plant_by_id = get_plant_by_id(plant_id)
        if plant_by_id is None:
            raise PlantNotFoundError(plant_id)
        else:
            return jsonify(plant_by_id)
    except PlantNotFoundError as e:
        return jsonify({"Error": e.message})


# API Route for a single plant data based on the plant name

@app.route('/api/plants/<string:plant_name>', methods=["GET"])
def get_plant_by_name_endpoint(plant_name):
    plant_by_name = get_plant_by_name(plant_name)
    return jsonify(plant_by_name)


# API route to add a plant to a collection that links it to the user
@app.route('/api/collection', methods=["POST"])
def add_plant_to_collection_endpoint():
    plant_collection_data = request.get_json()
    # how to get user_id, plant_id from plants.py
    # last_care can be date of adding to collection for starters (and later changed to user input)
    required_fields = ['user_id', 'plant_id', 'last_care']
    for field in required_fields:
        if field not in plant_collection_data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    last_care_date = plant_collection_data['last_care']
    plant = get_plant_by_id(plant_collection_data['plant_id'])
    care_frequency = plant['watering_frequency']
    upcoming_care_date = get_next_care_date(last_care_date, care_frequency)
    plant_collection_data['upcoming_care'] = upcoming_care_date
    add_plant_to_collection(plant_collection_data)
    return jsonify({"message": "Plant collection data added successfully."})

# API route to update last care and upcoming care date for specific plant and specific user
@app.route('/api/collection/care', methods=["PUT"])
def update_care():
    plant_to_update = request.get_json()
    required_fields = ['user_id', 'plant_id', 'last_care']
    for field in required_fields:
        if field not in  plant_to_update:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    last_care_date = plant_to_update['last_care']
    plant = get_plant_by_id( plant_to_update['plant_id'])
    care_frequency = plant['watering_frequency']
    upcoming_care_date = get_next_care_date(last_care_date, care_frequency)
    plant_to_update['upcoming_care'] = upcoming_care_date
    update_plant_in_collection( plant_to_update)
    return jsonify({"message": "Plant collection data has been updated successfully"})

# API route to get plant collection for a specific user
@app.route('/api/collection/<int:user_id>', methods=["GET"])
def get_plant_collection_by_user_endpoint(user_id):
    user_plant_collection = get_plants_in_user_collection(user_id)
    return jsonify(user_plant_collection)


# API route to get a specific plant from plant collection for a specific user
@app.route('/api/collection/<int:user_id>/<int:plant_id>/', methods=["GET"])
def get_plant_collection_by_ids_endpoint(user_id, plant_id):
     single_user_plant= get_plant_in_collection_by_id(user_id, plant_id)
     return jsonify(single_user_plant)

# API route to delete specific plant from plant-collection table for a specific user
class PlantDeletionError(Exception):
     def __init__(self, plant_id):
        self.plant_id = plant_id
        self.message = f"oops we are not able delete plant with ID {plant_id} from the collection."



@app.route('/api/collection/<int:user_id>/<int:plant_id>/', methods=["DELETE"])
def delete_plant_from_collection_endpoint(user_id, plant_id):
    try:

        check_plant_exists = get_plant_in_collection_by_id(user_id,plant_id)

        if check_plant_exists is None:
            raise PlantNotFoundError(plant_id)
        else:
            delete_plant = delete_plant_from_collection(user_id, plant_id)
            removed_plant = get_plant_by_id(plant_id)
            return jsonify({"message": f"The following plant {removed_plant['common_name']} with id {plant_id} has been deleted from plant collection.", "deleted": delete_plant}), 200
        
    except (PlantDeletionError, PlantNotFoundError) as e:
        return jsonify({"Error": e.message})




if __name__ == '__main__':
    app.run(port=3000,debug=True)
