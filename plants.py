from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/all_plants")
def all_plants():
    return render_template("all_plants.html")

if __name__ == '__main__':
    app.run(debug=True)

