# pip install Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


'''
To run the application, use the flask command or python -m flask. 
You need to tell the Flask where your application is with the --app option.

flask --app web run
'''