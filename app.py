from flask import Flask, render_template, request
from database_connect import DbConnectionError
from testusers import insert_new_record

import re

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
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

    return render_template('register.html', error=error, msg=success_msg)


if __name__ == "__main__":
    app.run(debug=True)
