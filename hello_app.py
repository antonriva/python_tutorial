from flask import Flask
from urllib.parse import quote as url_quote


app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>hello, world!</p>"
