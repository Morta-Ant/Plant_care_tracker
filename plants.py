from flask import Flask, render_template, redirect, session, request, url_for
import re, bcrypt
from database.crud_users import create_user, get_user_by_email
from database.database_connect import DbConnectionError
from database.crud_users import create_user
from database.config import SECRET_KEY
from database.crud_plants import get_all_plants, get_plant_by_id, get_plant_by_name
from database.crud_plant_collection import add_plant_to_collection, get_plants_in_user_collection
from flask_login import LoginManager
from utils.weather import WeatherInfo, DaylightInfo, get_weather_data

app = Flask(__name__)
app.secret_key = SECRET_KEY
login_manager = LoginManager

#index page
@app.route("/")
def index():
    return render_template("home.html")

# all plants page
@app.route("/plants")
def plants():
    try:
        plant_data = get_all_plants()  # Call your function to get plant data from the database
        return render_template("all_plants.html", data=plant_data)
    except Exception as e:
        return f"Oops! Something went wrong: {e}"

#individual plant pages    
@app.route("/plants/<int:id>")
def one_plant(id):
    try:
        plant_data = get_plant_by_id(id)  # Call your function to get plant data from the database
        if plant_data:
            return render_template("one_plant.html", **plant_data)
        else:
            return "Plant not found"
    except Exception as e:
        return f"Oops! Something went wrong: {e}"
 

#plant search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['search_query']
        results = get_plant_by_name(query)
        return render_template('search_results.html', results = results)
    else:
        return "Invalid request method. Please use the search bar to submit a query."
    
#registration
@app.route("/signup", methods=["GET","POST"])
def signup():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    success_msg = None
    error = None
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        if firstname == "" or len(firstname) < 3:
            error = 'Firstname must not be blank and should contain at least 3 characters'
        elif lastname == "" or len(lastname) < 3:
            error = 'Lastname must not be blank and should contain at least 3 characters'
        elif not re.fullmatch(regex, email):
            error = 'Invalid email'
        elif password == "" or len(password) < 6:
            error = 'Password must not be blank and should contain at least 6 characters'
        elif password != password2:
            error = 'Passwords must match'
        else:
            user = {
                'firstname': firstname,
                'lastname': lastname,
                'email': email,
                'passwd': password
            }

            try:
                create_user(user)
                success_msg = 'You have successfully registered!'
            except DbConnectionError:
                error = 'Failed to register due to a database connection error'

    return render_template('signup.html', error=error, msg=success_msg)


#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)
        if user is not None:
          passwordDB = user['passwd']
          is_password_correct = bcrypt.checkpw(password.encode("utf-8"), passwordDB.encode("utf-8"))
          if is_password_correct:
             session['loggedin'] = True
             session['id'] = user['user_id']
             session['email'] = user['email']
             session['firstname']=user['firstname']
             return redirect(url_for('collection'))
          else:
                error = 'Incorrect username or password, Please try again!'
        else:
            error = 'User not found!'

    return render_template("login.html", error=error)

#logout
@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('index'))

#collection
@app.route("/collection")
def collection():
    if "loggedin" in session:
        user_plants = get_plants_in_user_collection(session["id"])
        return render_template("collection.html", data = user_plants)
    return redirect(url_for("login"))

#add to collection
@app.route("/add_to_collection", methods=["POST"])
def add_to_collection():
    print(session)
    try:
        plant_id = request.form.get("plant_id")
        if plant_id is None:
            return "Invalid request"
        plant_collection = {
            "user_id": id,  
            "plant_id": plant_id,
            "last_care": None,  # Set this appropriately
            "upcoming_care": None,  # Set this appropriately
        }
        
        created_collection = add_plant_to_collection(plant_collection)
        if created_collection:
            return "Plant added to collection"
        else:
            return "Failed to add plant to collection"
    except Exception as e:
        return f"Failed to add plant to collection: {e}"
    

@app.route("/add_test_data", methods=["GET"])
def add_test_data():
    test_plant_collection = {
        "user_id": 1,
        "plant_id": 123,
        "last_care": "2023-08-16",
        "upcoming_care": "2023-08-23"
    }
    try:
        created_collection = add_plant_to_collection(test_plant_collection)
        if created_collection:
            return "Test data added to collection"
        else:
            return "Failed to add test data to collection"
    except Exception as e:
        return f"Failed to add test data to collection: {e}"

#get weather info
@app.route("/weather", methods=["POST"])
def weather_app():
    try:
        if request.method == "POST":
            city = request.form["city"]
            weather_data = get_weather_data(city)
            weather_info = WeatherInfo(weather_data)
            daylight_info = DaylightInfo(weather_data)
            return render_template("weather_results.html", city = city, weather_info = weather_info, daylight_info = daylight_info)
    except Exception as e:
        return f"Failed to retrieve the data: {e}"

if __name__ == '__main__':
    app.run(debug=True)
    
