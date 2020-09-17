from flask import Flask, request,render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>",404

@app.route('/test',methods=['GET',"POST"])
def getPage():
    return render_template('login_rawtest.html')

if __name__ == "__main__":
    app.run('0.0.0.0',port='8080')