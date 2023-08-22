from flask import Flask, render_template, request, session, redirect, url_for
import json, requests, re, bcrypt
from database.crud_users import create_user, DbConnectionError, get_user_by_email
from database.config import SECRET_KEY
from database.crud_plant_collection import get_plants_in_user_collection

app = Flask(__name__)
app.secret_key = SECRET_KEY


# index page
@app.route("/")
def index():
    return render_template("home.html")

# all plants page
@app.route("/plants")
def plants():
    try:
        data = requests.get("http://127.0.0.1:3000/api/plants").json()
        return render_template("all_plants.html", data = data)
    except requests.exceptions.JSONDecodeError:
        return "Oops! Something went wrong :("

#pages for individual plants
@app.route("/plants/<int:id>")
def one_plant(id):
    try:
        data = requests.get(f"http://127.0.0.1:3000/api/plants/{id}").json()
        return render_template("one_plant.html", **data)
    except requests.exceptions.JSONDecodeError:
        return "Oops! Something went wrong :("

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
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)
        # user format: (1, 'Name', 'Surname', 'email@email.com', '$2b$12$ewLJwOyJmENA3qyDBjchBe.Ceq9jJNNVGxC..uMPFrvhX7mBdZzHm')
        password_db = user['passwd']
        # checking if passwords match
        is_password_correct = bcrypt.checkpw(password.encode("utf-8"), password_db.encode("utf-8"))
        if is_password_correct:
            session['loggedin'] = True
            session['id'] = user['user_id']
            session['email'] = user['email']
            return render_template('home.html')
        else:
            msg = 'Incorrect username or password!'
    return render_template("login.html")


#logout
@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('index'))


#user collection
@app.route("/collection")
def user_collection():
    if "loggedin" in session:
        user_plants = requests.get(f"http://127.0.0.1:3000/api/collection/{session['id']}").json()
        return render_template("collection.html", data = user_plants)
    else:
        return redirect(url_for("login"))

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


if __name__ == '__main__':
    app.run(debug=True)

    

