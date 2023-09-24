from flask import Flask
from flask import render_template, url_for, request, jsonify
import requests
from Recommend import Recommend
from Movie import Movie
app = Flask(__name__)

thing = []
@app.route('/')
def index():
    message = "Hello from Flask!"
    return render_template('index.html', test=message)


@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    # Process the data as needed
    response_data = {"message": "Data received successfully"}
    unique_set = set(data)
    data = list(unique_set)
    for i in data:
        rec = Recommend(i)
        thing.append(Movie(rec.getRecTitles2(i)[0]))
        thing.append(Movie(rec.getRecTitles2(i)[1]))

    print(thing[0])
    
    
    return jsonify(data)

@app.route('/output')
def output():
    return render_template("output.html", 
                           t1=thing[0].movie_title,
                           re1="",
                           r1="",
                           d1="",
                           t2=thing[1].movie_title,
                           re2="",
                           r2="",
                           d2="",
                           t3=thing[2].movie_title,
                           re3="",
                           r3="",
                           d3="",

)

@app.route("/moviepage")
def moviepage():
    return render_template("moviepage.html", name="1", releaseDate="2", rating="3", tags="4", description="5", cast="6")

if __name__ == '__main__':
    app.run(debug=True)

