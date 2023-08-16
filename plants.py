from flask import Flask, render_template, redirect, session, request, url_for,g
import json, re, bcrypt
from database.users import insert_new_record, DbConnectionError, get_user_by_email
from database.crud_users import create_user,get_user_by_id
from database.config import SECRET_KEY
from database.crud_plants import get_all_plants,get_plant_by_id
from database.crud_plant_collection import create_plant_collection
from flask_login import current_user, LoginManager

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
             session['email'] = user['email']
             session['firstname']=user['firstname']
             success_msg="You are now logged in"
             return redirect(url_for('collection'),msg=success_msg)#('home.html',msg=success_msg)
          else:
                error = 'Incorrect username or password, Please try agaib!'
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
    
    return render_template("collection.html")
#########ADD to Collection
#@app.route("/plants/<int:id>"


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
        
        created_collection = create_plant_collection(plant_collection)
        if created_collection:
            return "Plant added to collection"
        else:
            return "Failed to add plant to collection"
    except Exception as e:
        return f"Failed to add plant to collection: {e}"
    

#user collection
@app.route("/<user>/collection")
def user_collection():
    pass

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
if __name__ == '__main__':
    app.run(debug=True)
    

