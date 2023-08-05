from flask import Flask, render_template, request
from data import data

app = Flask(__name__)

def search_data(query):
    results = []
    for item in data:
        # Convert all string values in the dictionary to lowercase and check for the query.
        if any(str(value).lower().count(query.lower()) > 0 for value in item.values()):
            results.append(item)
    return results


# Route to render the search bar on the index page.
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the search query and display search results.
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['search_query']
        results = search_data(query)
        return render_template('search_results.html', results=results)
    else:
        return "Invalid request method. Please use the search bar to submit a query."



if __name__ == '__main__':
    app.run(debug=True)
