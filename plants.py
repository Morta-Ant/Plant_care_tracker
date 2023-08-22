from flask import Flask, render_template, redirect, session, request, url_for,g,flash
import json, re, bcrypt
from database.users import insert_new_record, DbConnectionError, get_user_by_email
from database.crud_users import create_user,get_user_by_id
from database.config import SECRET_KEY
from database.crud_plants import get_all_plants,get_plant_by_id,get_plant_by_name,get_connector
from database.crud_plant_collection import create_plant_collection,get_all_plant_collections
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
                insert_new_record(user)
                success_msg = 'You have successfully registered!'
            except DbConnectionError:
                error = 'Failed to register due to a database connection error'

    return render_template('signup.html', error=error, msg=success_msg)


#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    success_msg = None
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)
        # checking if passwords match
        if user is not None:  # Check if user exists
          is_password_correct = bcrypt.checkpw(password.encode("utf-8"), user['passwd'].encode("utf-8")) #password_db.encode("utf-8"))
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

# Add a new route to display an individual user's plant collection
# @app.route("/collection/<int:user_id>/<int:plant_id>")
# def user_collection(user_id, plant_id):
#     try:
#         if "loggedin" in session:
#             user_plant_collection = get_plant_collection_by_ids(user_id, plant_id)

#             return render_template("user_collection.html", collection=user_plant_collection)
#     except Exception as e:
#         return f"Oops! Something went wrong: {e}"



# @app.route("/collection")
# def collection():
#   try:
#     if "loggedin" in session:
#         user_plants =get_all_plant_collections()
#         plant_data = get_all_plants()
#         print("Calling get_all_plant_collections()")
#         print("This is the data",user_plants)#data returned is none how to get data
#         print("Data in collection route:", user_plants)
#         #user_plants = requests.get(f"http://127.0.0.1:3000/api/collection/{session['id']}").json()
#         return render_template("collection.html", data = user_plants,plant_data=plant_data)
     
#   except Exception as e:
#         return f"Oops! Something went wrong: {e}"
#########ADD to Collection
#@app.route("/plants/<int:id>"
def plants():
    try:
        plant_data = get_all_plants()  # Call your function to get plant data from the database
        return render_template("all_plants.html", data=plant_data)
    except Exception as e:
        return f"Oops! Something went wrong: {e}"


@app.route("/add_to_collection", methods=["POST"])
def add_to_collection():
    # Check if the user is logged in
    if not session.get('loggedin'):
        return "You need to log in to add plants to your collection."

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
        created_collection = create_plant_collection(test_plant_collection)
        if created_collection:
            return "Test data added to collection"
        else:
            return "Failed to add test data to collection"
    except Exception as e:
        return f"Failed to add test data to collection: {e}"
    
# http://localhost:5000/profile - this will be the profile page, only accessible for logged in users
@app.route('/profile')
def profile():
    # Check if the user is logged in
    if 'loggedin' in session:
        # Get the user ID from the session
        user_id = session.get('id')
        
        # Retrieve user information by their ID
        user = get_user_by_id(user_id)
        
        # Check if the user exists
        if user:
            return render_template('profile.html', user=user)
        else:
            return "User not found"
    
    # User is not logged in, redirect to the login page
    return redirect(url_for('login'))
	

if __name__ == '__main__':
    app.run(debug=True)
    

