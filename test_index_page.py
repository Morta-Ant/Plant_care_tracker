import unittest
from unittest import TestCase, main
from plants import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_page(self):
        response = self.client.get('/')
        print(response.status_code)  # Print the response status code
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
