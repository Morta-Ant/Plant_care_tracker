import unittest
from unittest import TestCase, main
from plants import app




class TestSearchRoute(unittest.TestCase):

        def setUp(self):
            app.config['TESTING'] = True
            self.app = app.test_client()

        def test_search_for_existing_plant(self):
            data = {'search_query': 'Snake Plant'}
            response = self.app.post('/search', data=data, follow_redirects=True)
            print(response.status_code)
            print(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Snake Plant', response.data)

        def test_search_for_non_existing_plant(self):
            data = {'search_query': 'Blueberry'}
            response = self.app.post('/search', data=data, follow_redirects=True)
            print(response.status_code)
            print(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'No results found', response.data)

        def test_search_for_more_than_one_result(self):
            data = {'search_query': 'Spider Plant'}
            response = self.app.post('/search', data=data, follow_redirects=True)
            print(response.status_code)
            print(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Spider Plant', b'Spider Plant (Variegated)', response.data)

        def test_search_for_incomplete_name_searched(self):
            data = {'search_query': 'Jade'}
            response = self.app.post('/search', data=data, follow_redirects=True)
            print(response.status_code)
            print(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Jade Plant', response.data)


if __name__ == '__main__':
    unittest.main()


