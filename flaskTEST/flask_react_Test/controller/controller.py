from flask import Flask,Blueprint,render_template,jsonify,redirect,url_for,request,make_response,request
from model.mapinfo import mapinfo
from model.measureInfo import meausreInfo
main_view = Blueprint('mains',__name__)

@main_view.route("/load_map", methods=['POST','GET'])
def load_map():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        if data == None:
            print(request.headers)
        map_number = data['map_id']
        map_info = mapinfo.get(map_number)
        return jsonify(map_info)

@main_view.route("/load_measure",methods=['POST',"GET"])
def load_info():
    if request.method == "GET":
        data = request.args.get("map_id")
        print("param : ",data)
        if data == None:
            print(request.headers)
        meausre_info = meausreInfo.get(data)
        return jsonify(meausre_info)
        
