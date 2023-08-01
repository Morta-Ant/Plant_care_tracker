from flask import Flask, render_template, request
import json
import requests


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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


@app.route("/signup", methods=["POST"])
def signup():
    pass

@app.route("/login", methods=["GET", "POST"])
def login():
    pass

@app.route("/<user>/collection")
def user_collection():
    pass

@app.route("/<user>/collection/<id>")
def user_plant(id):
    pass

if __name__ == '__main__':
    app.run(debug=True)
    

