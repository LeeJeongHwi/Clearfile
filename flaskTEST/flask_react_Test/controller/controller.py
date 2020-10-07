from flask import Flask,Blueprint,render_template,jsonify,redirect,url_for,request,make_response,request
from model.mapinfo import mapinfo

main_view = Blueprint('mains',__name__)

@main_view.route("/load_map", methods=['POST','GET'])
def load_mpa():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        map_number = int(data['map_id'])
        map_info = mapinfo.get(map_number)
        return jsonify(map_info)

@main_view.route("/")
def main_page():
    return render_template('test.html')
