from unittest import TestCase,main
from plants import app  # Import your Flask app instance

class TestSignup(TestCase):

    def setUp(self):#Setup the testing environment
        app.config['TESTING'] = True # set Flask into test mode to use the test client
        self.app = app.test_client()# Using test_client to simulate HTTP requests 

    def test_signup_valid(self):#Test for a valid sign up
        data = {
            'firstname': 'Bill',
            'lastname': 'Bolt',
            'email': 'BBolt@gmail.com',
            'password': 'Tiger123',
            'password2': 'Tiger123'
        }
        response = self.app.post('/signup', data=data, follow_redirects=True)
        print(response.status_code)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have successfully registered!', response.data)
    
    def test_firstname_blank(self):#Test for a blank firstname
        data = {
            'firstname': '',  # Blank firstname
            'lastname': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'SecretPass123',
            'password2': 'SecretPass123'
        }
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
       
        self.assertIn(b'Firstname must not be blank', response.data)
    
    def test_firstname_too_short(self):#Test the length of the firstname
        data = {
            'firstname':'Bo',  # firstname too short
            'lastname': 'Smith',
            'email': 'Bob.smith@example.com',
            'password': 'Password123',
            'password2': 'Password123'
        }
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Firstname must not be blank and should contain at least 3 characters', response.data)

    def test_invalid_email(self):#Test for an invalid email
        data = {
            'firstname':'Monica',  
            'lastname': 'Wade',
            'email': 'Mwadehotmail.com',# Invalid email
            'password': 'Password123',
            'password2': 'Password123'
        }
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid email', response.data)
   

    def test_for_blank_password(self):#Test for blank password
        data = {
            'firstname':'May',  
            'lastname': 'Wright',
            'email': 'Maywrigh@gmail.com',
            'password': '',    #blank password
            'password2': 'Nightshift'
        }
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Password must not be blank and should contain at least 6 characters', response.data)



    def test_password_length(self):#Test for password length
        data = {
            'firstname':'May',  # firstname too short
            'lastname': 'Wright',
            'email': 'Maywright@gmail.com',
            'password': 'Night',
            'password2': 'Nightshift'
        }
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Password must not be blank and should contain at least 6 characters', response.data)

    def test_passwords_match(self):#Test passwords match
        data = {
            'firstname':'Brandon', 
            'lastname': 'Thomas',
            'email': 'Bthomas@gmail.com',
            'password': 'Sharper', #password do not match
            'password2': 'Sharppe' #password do not match
        }
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Passwords must match', response.data)


if __name__ == '__main__':
   main()


