from flask import Blueprint,request,render_template,flash,redirect,url_for
from flask import current_app as app

main = Blueprint('main',__name__, url_prefix='/') 
# index 파일을 들어갔을 때 이름 설정할지 결정하는 부분 / prefix는 URL을 어떻게 뒤에 붙일지 결정하는 부분

@main.route('/main',methods=['GET'])  # 파일 내부에서 어떤 경로로 나타낼지 결정하는 부분
def index():
    testData = "testData Array" #html 파일에 전달하고자 하는 데이터 ==> 주로 String, Dict를 전송함
    return render_template('/main/index.html', testDataHtml = testData) #추후에 url_for에서 사용될 함수 이름
