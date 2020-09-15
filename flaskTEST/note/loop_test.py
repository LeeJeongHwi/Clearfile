from flask import render_template,Flask

app = Flask(__name__)

@app.route('/loop_test')
def loops():
    values = ['1','2','3']
    return render_template('loop.html',values=values)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
    