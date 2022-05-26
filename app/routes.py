from flask import Flask 


app = Flask(__name__)


@app.get("/")
def index():
    me = {
        "first_name": "Savannah",
        "last_name": "Germino",
        "hobbies": "Reading"
    }
    return me



    