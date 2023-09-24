from flask import Flask
from flask import render_template, url_for, request, jsonify
import requests
from Recommend import Recommend
import time
from Movie import Movie
app = Flask(__name__)

thing=[]
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

    thing.clear()
    print(thing)
    data = request.get_json()
    unique_set = set(data)
    data = list(unique_set)
    for i in range (4):
        rec = Recommend(data[i])
        rec.getRecTitles2(data[i])[0]
        rec.getRecTitles2(data[i])[1]
        thing.append(Movie(rec.getRecTitles2(data[i])[0]))
        thing.append(Movie(rec.getRecTitles2(data[i])[1]))
        print("//////////////////////////////////////////////////////////////////")
        print(thing)
    
    
    for item in thing:
        print(item.movie_title)
    
    return jsonify(data)

@app.route('/output')
def output():
    return render_template("output.html", 
                           t1=thing[0].movie_title,
                           re1=thing[0].release,
                           r1="",
                           d1=thing[0].movie_plot,
                           t2=thing[1].movie_title,
                           re2=thing[1].release,
                           r2="",
                           d2=thing[1].movie_plot,
                           t3=thing[2].movie_title,
                           re3=thing[2].release,
                           r3="",
                           d3=thing[2].movie_plot,
                           t4=thing[3].movie_title,
                           re4=thing[3].release,
                           r4="",
                           d4=thing[3].movie_plot,
                           t5=thing[4].movie_title,
                           re5=thing[4].release,
                           r5="",
                           d5=thing[4].movie_plot,
                           i0 = thing[0].images,
                           i1 = thing[1].images,
                           i2 = thing[2].images,
                           i3 = thing[3].images,
                           i4 = thing[4].images
                           )


@app.route("/moviepage")
def moviepage():
    return render_template("moviepage.html", name="1", releaseDate="2", rating="3", tags="4", description="5", cast="6")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

