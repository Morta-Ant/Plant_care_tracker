import unittest
from unittest import TestCase, main
from database.config import SECRET_KEY
from flask import Flask,request
from plants import signup  # Import your Flask app instance

app = Flask(__name__)
app.secret_key = SECRET_KEY
       
class TestSignup(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def test_signup_valid(self):
        data = {
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'SecurePass123',
            'password2': 'SecurePass123'
        }
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have successfully registered!', response.data)

    def test_signup_invalid(self):
        data = {
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'invalid_email',  # Invalid email
            'password': 'short',  # Password too short
            'password2': 'mismatch'  # Passwords don't match
        }
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid email', response.data)
        self.assertIn(b'Password must not be blank and should contain at least 6 characters', response.data)
        self.assertIn(b'Passwords must match', response.data)

if __name__ == '__main__':
    unittest.main()
