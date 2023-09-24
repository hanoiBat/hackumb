from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    message = "Hello from Flask!"
    return render_template('index.html', test=message)


@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')
    

if __name__ == '__main__':
    app.run(debug=True)
