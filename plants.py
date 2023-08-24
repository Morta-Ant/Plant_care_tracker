from flask import Flask, render_template, redirect, session, request, url_for,g,flash
import json, re, bcrypt, requests, datetime as dt
from database.crud_users import create_user, get_user_by_email
from database.database_connect import DbConnectionError
from database.crud_users import create_user,get_user_by_id
from database.config import SECRET_KEY
from database.crud_plants import get_all_plants, get_plant_by_id
from database.crud_plant_collection import add_plant_to_collection,get_all_plant_collections
from database.crud_plant_collection import get_plants_in_user_collection,create_plant_collection

from flask_login import current_user, LoginManager
from datetime import datetime,timedelta

app = Flask(__name__)
app.secret_key = SECRET_KEY
login_manager = LoginManager

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/plants")
def plants():
    try:
        plant_data = get_all_plants()  # Call your function to get plant data from the database
        return render_template("all_plants.html", data=plant_data)
    except Exception as e:
        return f"Oops! Something went wrong: {e}"
    
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
 

#pages for individual plants

#search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['search_query']
        results = search_data(query)
        return render_template('search_results.html', results=results)
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
        # user format: (1, 'Name', 'Surname', 'email@email.com', '$2b$12$ewLJwOyJmENA3qyDBjchBe.Ceq9jJNNVGxC..uMPFrvhX7mBdZzHm')
        if user is not None:  # Check if user exists
          passwordDB = user['passwd']
          is_password_correct = bcrypt.checkpw(password.encode("utf-8"), passwordDB.encode("utf-8"))
          if is_password_correct:
             session['loggedin'] = True
             session['id'] = user['user_id']
            # session['user_id'] = user[email]['user_id']
             session['email'] = user['email']
             session['firstname']=user['firstname']
             success_msg="You are now logged in"

             return redirect(url_for('collection'),success_msg)

        

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


# Python code to pre-process the data

@app.route("/collection")
def collection():
    error = None
    user_id = session.get('id')
    if "loggedin" not in session:
        flash("You need to log in to access the Collection.", 'error')
        return redirect(url_for('index'))
    try:
        if "loggedin" in session:
            user_plants = get_all_plant_collections()
            plant_data = get_all_plants()
            
            # Pre-process data to match plant information with care information
            pre_processed_data = []
            for care_info in user_plants:
                matching_plant = next((plant for plant in plant_data if plant['plant_id'] == care_info['plant_id']), None)
                if matching_plant:
                    pre_processed_data.append({
                        'plant': matching_plant,
                        'care_info': care_info
                    })
            print(pre_processed_data)
            return render_template("collection.html", data=pre_processed_data,error=error)
    except Exception as e:
        return f"Oops! Something went wrong: {e}"


def plants():
    try:
        plant_data = get_all_plants()  # Call your function to get plant data from the database
        return render_template("all_plants.html", data=plant_data)
    except Exception as e:
        return f"Oops! Something went wrong: {e}"

#collection There are ARE TWO COLLECTION FUNCTIONS
# @app.route("/collection")
# def collection():
#     if "loggedin" in session:
#         user_plants = get_plants_in_user_collection(session["id"])
#         return render_template("collection.html", data = user_plants)
#     return redirect(url_for("login"))

@app.route("/add_to_collection", methods=["POST"])
def add_to_collection():
    error = None
    # Check if the user is logged in
    if not session.get('loggedin'):
        flash("You need to log in to add plants to your collection.")
        return redirect(url_for('index'))
    # Get the user_id from the session
    user_id = session.get('id')

    try:
        plant_id = request.form.get("plant_id")

        if plant_id is None:
            return "Invalid request"

        # Create a plant_collection dictionary
        plant_collection = {
            "user_id": user_id,
            "plant_id": plant_id,
            "last_care": datetime.now(),  # Set this to the current datetime
            "upcoming_care": datetime.now() + timedelta(days=7),  # Set this to the current datetime plus 7 days
        }


        # Call the create_plant_collection function to insert the record into the database
        created_collection = create_plant_collection(plant_collection)


        if created_collection:
            return redirect(url_for('collection'))  # Redirect to the collection page
        else:
            return "Failed to add plant to collection"

    except Exception as e:
        return f"Failed to add plant to collection: {e}"


# #user collection
# @app.route("/<user>/collection")
# def user_collection():
#     pass

#individual plant within user's collection
@app.route("/<user>/collection/<id>")
def user_plant(id):
    pass

#currently search searches the json file, should pull from database via plant-care-api
def search_data(query):
    results = []
    with open("database/plant_care_data.json") as plant_data:
        data = json.load(plant_data)
    for item in data:
        # Convert all string values in the dictionary to lowercase and check for the query.
        if any(str(value).lower().count(query.lower()) > 0 for value in item.values()):
            results.append(item)
    return results

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

#weather api search bar
def get_weather(city):
    open_weather = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = '****'

    url = open_weather + "appid=" + api_key + "&q=" + city

    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    temp_fahrenheit = temp_celsius * (9 / 5) + 32
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius = feels_like_kelvin - 273.15
    feels_like_fahrenheit = feels_like_celsius * (9 / 5) + 32
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    weather_info = [
        f"Temperature in {city}: {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F",
        f"Temperature in {city} feels like {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F",
        f"General Weather in {city}: {description}",
        f"Sun Rises in {city} at {sunrise_time} local time.",
        f"Sun Sets in {city} at {sunset_time} local time."
    ]

    return weather_info

@app.route("/", methods=["GET", "POST"])
def weather_app():
    if request.method == "POST":
        city = request.form["city"]
        weather_info = get_weather(city)
        return render_template("weather_results.html", weather_info=weather_info)
    return render_template("weather_form.html")

if __name__ == '__main__':
    app.run(debug=True)
    
