from unittest import TestCase,main
from plants import app  # Import your Flask app instance
from bs4 import BeautifulSoup

class TestNavigation(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass
  
    def test_index_route(self):
        response = self.app.get('/')
        assert response.status_code == 200  # Check if the route returns 200 OK
        soup = BeautifulSoup(response.data, 'html.parser')
        #Check if the page title is as expected
        page_title = soup.title.string
        self.assertEqual(page_title, 'Home') 

    def test_plants_route(self):
        response = self.app.get('/plants')
        assert response.status_code == 200  # Check if the route returns 200 OK
        soup = BeautifulSoup(response.data, 'html.parser')
        #Check if the page title is as expected
        page_title = soup.title.string
        self.assertEqual(page_title, 'All Plants') 


    def test_signup_route(self):
        response = self.app.get('/signup')
        assert response.status_code == 200  # Check if the route returns 200 OK
        soup = BeautifulSoup(response.data, 'html.parser')
        #Check if the page title is as expected
        page_title = soup.title.string
        self.assertEqual(page_title, 'Sign up') 

    def test_login_route(self):
        response = self.app.get('/login',follow_redirects=True)
        assert response.status_code == 200  # Check if the route returns 200 OK
        #Parse the HTML content of the response
        soup = BeautifulSoup(response.data, 'html.parser')
        #Check if the page title is as expected
        page_title = soup.title.string
        self.assertEqual(page_title, 'Login') 

    def test_logout_route(self):
        response = self.app.get('/logout',follow_redirects=True)
        assert response.status_code == 200   #  Check if the route returns a redirect (200)
        soup = BeautifulSoup(response.data, 'html.parser')
        #Check if the page title is as expected
        page_title = soup.title.string
        self.assertEqual(page_title, 'Home') #When the user selects logout they are directed to the home page


    def test_collection_route(self):
        response = self.app.get('/collection',follow_redirects=True)
        assert response.status_code == 200   #Check if the route returns 200 OK
        #Parse the HTML content of the response
        soup = BeautifulSoup(response.data, 'html.parser')
        # Check if the page title is as expected
        page_title = soup.title.string
        self.assertEqual(page_title, 'Login')#the collection page goes to the login page from the navi bar unless the user is logged in
       

    def test_add_to_collection_route(self):
        response = self.app.post('/add_to_collection',follow_redirects=True)
        assert response.status_code == 200 
        #Parse the HTML content of the response
        soup = BeautifulSoup(response.data, 'html.parser')
        # Check if the page title is as expected
        page_title = soup.title.string
        self.assertEqual(page_title, 'Login')#goes to the login page if the user is not logged in
  

if __name__ == '__main__':
    main()