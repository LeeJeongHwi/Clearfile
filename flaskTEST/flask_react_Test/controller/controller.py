from flask import Flask,Blueprint,render_template,jsonify,redirect,url_for,request,make_response,request
from model.mapinfo import mapinfo
from model.markerInfo import markerInfo
main_view = Blueprint('mains',__name__)

@main_view.route("/load_map", methods=['POST','GET'])
def load_map():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        if data == None:
            print(request.headers)
        map_number = int(data['map_id'])
        map_info = mapinfo.get(map_number)
        return jsonify(map_info)

@main_view.route("/get_info", methods=["POST","GET"])
def get_info():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        if data == None:
            print(request.headers)
        marker_number = int(data["marker_id"])
        marker_info = markerInfo.get(marker_number)
        