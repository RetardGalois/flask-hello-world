from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get("http://google.com.br")
    return r.text
