from unittest import TestCase,main
from plants import app  # Import your Flask app instance
from database.crud_users import get_user_by_email
from flask import url_for
class TestLoginRoute(TestCase):


    def setUp(self):#Setup the testing environment
        app.config['TESTING'] = True # set Flask into test mode to use the test client
        self.app = app.test_client()# Using test_client to simulate HTTP requests 

    def test_login_successful(self):
        #a valid user for testing
        user_data = {
            'email': 'ssmith@hotmail.com',
            'password': 'test123'
        }

        response = self.app.post('/login', data=user_data)
    
       
        self.assertTrue(response.status_code in (302, 308))  # Check for a redirect status code
       # self.assertEqual(response.location, 'http://localhost/login/')  # Check the redirection URL
    
    def test_login_blank_fields(self):
            # Simulate a login request with blank fields
            blank_data={
                 'email':'',
                 'password': ''
            } 
            response = self.app.post('/login', data=blank_data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)  # Check if status code is OK
            self.assertIn(b'Email and password are required fields',response.data)# Expected error message
             
             
    def test_login_invalid_credentials(self):
        # Test with invalid details
        invalid_user_data = {
            'email': 'gail@hotmail.com',
            'password': 'rest123'
        }

        response = self.app.post('/login', data=invalid_user_data, follow_redirects=True)        
        self.assertEqual(response.status_code, 200)  
        # Assert that the user sees an error message on the login page
        self.assertIn(b'User not found!', response.data)  # Expected error message

if __name__ == '__main__':
    main()                                                              