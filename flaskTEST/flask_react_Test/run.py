from flask import Flask,jsonify,Blueprint,request,make_response
from flask_cors import CORS
import os
from controller import controller as ctr

app = Flask(__name__)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
CORS(app)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(ctr.main_view,url_prefix='/')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080',debug=True)