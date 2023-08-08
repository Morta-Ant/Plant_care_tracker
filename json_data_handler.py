from database.crud_plants import create_plant
import json

# plant care data
with open("database/plant_care_data.json") as plants_care:
    plant_data = json.load(plants_care)

for plant in plant_data:
    print(f"Creating plant {plant['common_name']} with id {plant['plant_id']}...")
    create_plant(plant)