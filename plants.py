from flask import Flask, render_template, redirect, session, request, url_for, flash
import json, re, bcrypt
from database.crud_users import create_user, get_user_by_email
from database.database_connect import DbConnectionError
from database.crud_users import create_user
from database.config import SECRET_KEY
from database.crud_plants import get_all_plants, get_plant_by_id, get_plant_by_name
from database.crud_plant_collection import add_plant_to_collection,get_plants_data_in_user_collection,add_plant_to_collection, get_user_collection,update_plant_in_collection, delete_plant_from_collection
from flask_login import LoginManager
from utils.weather import WeatherInfo, DaylightInfo, get_weather_data
from utils.get_next_care_date import is_next_care_date_up_to_date, get_next_care_date
from datetime import datetime,timedelta

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
 

#search
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
            # session['user_id'] = user[email]['user_id']
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



@app.route("/collection")
def collection():
    if "loggedin" in session:
        try:
            user_collection = get_user_collection(session["id"])
            # Check if any care dates need updating        
            for entry in user_collection:
                if not is_next_care_date_up_to_date(entry["upcoming_care"]):
                    updated_collection_entry = {}
                    updated_collection_entry["user_id"] = session["id"]
                    updated_collection_entry["plant_id"] = entry["plant_id"]
                    updated_collection_entry["last_care"] = entry["upcoming_care"]
                    watering_frequency = get_plant_by_id(entry["plant_id"])["watering_frequency"]
                    new_upcoming_care = get_next_care_date(entry["upcoming_care"], watering_frequency)
                    updated_collection_entry["upcoming_care"] = new_upcoming_care
                    update_plant_in_collection(updated_collection_entry)

            user_plants = get_plants_data_in_user_collection(session["id"])
            print(user_plants)
            return render_template("collection.html", data = user_plants)
        except Exception as e:
            return f"Oops! Something went wrong: {e}"
    else:
        flash("You need to log in to access the Collection.", 'error')
        return redirect(url_for('login'))

#add to collection
@app.route("/add_to_collection", methods=["POST"])
def add_to_collection():
    # Check if the user is logged in
    if not session.get('loggedin'):
        flash("You need to log in to add plants to your collection.")
        return redirect(url_for('login'))
    # Get the user_id from the session
    user_id = session.get('id')

    try:
        plant_id = request.form.get("plant_id")

        if plant_id is None:
            return "Invalid request"

        # Get care dates
        last_care = datetime.now()
        watering_frequency = get_plant_by_id(plant_id)["watering_frequency"]
        upcoming_care = get_next_care_date(last_care,watering_frequency)
        plant_collection = {
            "user_id": user_id,
            "plant_id": plant_id,
            "last_care": last_care,
            "upcoming_care": upcoming_care
        }

        # Call the create_plant_collection function to insert the record into the database
        add_plant_to_collection(plant_collection)
        return redirect(url_for('collection'))  # Redirect to the collection page

    except Exception as e:
        return f"Failed to add plant to collection: {e}"
    
# remove from collection
@app.route("/remove_from_collection", methods=["POST"])
def remove_from_collection():
    user_id = session.get('id')
    try:
        plant_id = request.form.get("plant_id", type=int)
        delete_plant_from_collection(user_id, plant_id)
        return redirect(url_for("collection"))
    except Exception as e:
        return f"failed to remove from collection: {e}"


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
        "plant_id": 9,
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
    
