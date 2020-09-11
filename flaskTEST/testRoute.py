from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World!"

@app.route('/test/<username>')
def get_progilfe(username):
    return "profile"+username

if __name__ == '__main__':
    app.run(host="localhost",port="8080")