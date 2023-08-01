from plant_care_data import plant_data
import crud_plants

for plant in plant_data:
    print(f"Creating plant {plant['common_name']} with id {plant['plant_id']}...")
    crud_plants.create_plant(plant)