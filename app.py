from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Flask Crud API"

@app.route("/home")
def home():
    return "Home Page"