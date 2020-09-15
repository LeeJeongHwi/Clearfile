from flask import Flask,jsonify,request,render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/login')
def login():
    email_address = request.args.get('email_address')
    passwd = request.args.get('passwd')
    print(email_address,passwd)
    if email_address == 'wjdgnl97@gmail.com':
        return_data = {'auth':'success'}
    else:
        return_data = {'auth':'failed'}
    return jsonify(return_data)

@app.route('/html_test')
def hello_html():
    return render_template('login_rawtest.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')