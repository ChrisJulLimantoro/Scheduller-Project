from flask import *

app = Flask(__name__)

@app.route("/")
def testing():
    return "<h1>hallo ngabb!</h1>"