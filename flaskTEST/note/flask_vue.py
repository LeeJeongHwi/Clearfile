from flask import Flask,render_template,make_response,request,jsonify
from flask_cors import CORS
app= Flask(__name__)
CORS(app)

@app.route('/test',methods=['GET',"POST"])
def test():
    if request.method=='POST':
        print("POST")
        data= request.get_json()
        print(data)
        print(data['email'])
    if request.method=='GET':
        print("GET")
        user = request.args.get("email")
    return make_response(jsonify(status=True),200)

if __name__ == "__main__":
    app.run('0.0.0.0',port='8080')