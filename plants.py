from flask import Flask, render_template, request
import json
import requests
from users import insert_new_record, DbConnectionError
import re


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/plants")
def plants():
    try:
        data = requests.get("http://127.0.0.1:3000/api/plants").json()
        return render_template("all_plants.html", data = data)
    except requests.exceptions.JSONDecodeError:
        return "Oops! Something went wrong :("

@app.route("/plants/<int:id>")
def one_plant(id):
    try:
        data = requests.get(f"http://127.0.0.1:3000/api/plants/{id}").json()
        return render_template("one_plant.html", **data)
    except requests.exceptions.JSONDecodeError:
        return "Oops! Something went wrong :("

@app.route('/search', methods=['GET', 'POST'])
def search():
    pass


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


@app.route("/login", methods=["GET", "POST"])
def login():
     return render_template('login.html')

@app.route("/<user>/collection")
def user_collection():
    pass

@app.route("/<user>/collection/<id>")
def user_plant(id):
    pass

if __name__ == '__main__':
    app.run(debug=True)
    

