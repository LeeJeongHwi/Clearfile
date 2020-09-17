from flask import Flask
import requests

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    print("Before first request")

@app.before_request
def before_request():
    print("Before Request")

@app.after_request
def after_request(response):
    print("After Request")
    return response

@app.route("/test")
def tests():
    print("Hello")
    return "<h1>Hello Flaks!</h1>"

if __name__ == "__main__":
    app.run('0.0.0.0',port='8080')