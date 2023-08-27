import uuid
import unittest
import datetime
import database.database_connect
from database.crud_users import get_user_by_id, create_user, delete_user
from database.crud_plants import get_plant_by_id, create_plant, delete_plant
from database.crud_plant_collection import add_plant_to_collection, delete_plant_from_collection, get_plant_in_collection_by_ids

class TestConnection(unittest.TestCase):
    connection = None
    def setUp(self):
         self.connection = database.database_connect.get_connector()

    def tearDown(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def test_connection(self):
        self.assertTrue(self.connection.is_connected())

def generate_test_user():
    test_user = {"user_id": 0,
                "firstname": "Test",
                "lastname": "Testing",
                "email": f"test{uuid.uuid4()}@test.com",
                "passwd": "testy"
    }
    return test_user

def generate_test_plant():
    test_plant = {
            "plant_id": 0,
            "common_name": "Plant Test",
            "scientific_name": "Testaveria test",
            "other_name": "Test plant",
            "light_level": "test",
            "watering_frequency": 1,
            "growth_rate": "test",
            "maintenance_level": "test",
            "plant_description": "This description is also a test.",
            "image": "https://test-url.com"
    }
    return test_plant

class TestCreateDeletePlant(unittest.TestCase):
    def test_create_delete(self):
        plant = generate_test_plant()
        created_plant = create_plant(plant)
        created_plant_id = created_plant["plant_id"]

        self.assertIsNot(0, created_plant_id)

        delete_plant(created_plant_id)
        plant_exists = get_plant_by_id(created_plant_id)

        self.assertIsNone(plant_exists)

class TestCreateDeleteUser(unittest.TestCase):
    def test_create_delete(self):
        user = generate_test_user()
        created_user = create_user(user)
        created_user_id = created_user["user_id"]

        self.assertIsNot(0, created_user_id)

        delete_user(created_user_id)
        user_exists = get_user_by_id(created_user_id)

        self.assertIsNone(user_exists)

class TestCreateDeleteCollection(unittest.TestCase):
    def test_create_delete(self):
        user = create_user(generate_test_user())
        plant = create_plant(generate_test_plant())
        
        user_collection = {"user_id": user["user_id"],
                           "plant_id": plant["plant_id"],
                           "last_care": datetime.datetime.now().replace(microsecond=0), # Used to remove miliseconds in order to compare to the database object
                           "upcoming_care": datetime.datetime.now().replace(microsecond=0)
        }

        created_collection = add_plant_to_collection(user_collection)
        created_collection_from_db = get_plant_in_collection_by_ids(user["user_id"], plant["plant_id"])

        self.assertEqual(created_collection, created_collection_from_db)

        delete_plant_from_collection(user["user_id"], plant["plant_id"])
        created_collection_from_db = get_plant_in_collection_by_ids(user["user_id"], plant["plant_id"])

        self.assertIsNone(created_collection_from_db)

        delete_user(user["user_id"])
        delete_plant(plant["plant_id"])


if __name__ == '__main__':
    unittest.main()
