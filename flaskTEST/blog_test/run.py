from flask import Flask,jsonify,request,make_response,Blueprint
from flask_login import LoginManager,current_user,login_required,login_user,logout_user
from flask_cors import CORS # 다른 프론트 엔드를 쓸 때 사용(나는 리액트)
#oauth2 --> social Login 할 때 사용
import os
from blog_control import user_mgmt
from blog_view import blog

# https 만을 지원하는 기능을 http 에서 테스트 할 때 필요한 설정

os.environ['OAUTHLIB_INSECURE_TRANSPPORT'] = '1'

#static_url_path : static 주소
app = Flask(__name__,static_url_path='/static')
CORS(app) # 리액트와 연동
app.secure_key = 'Lee_Server' # 테스트를 위한 고정값

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) # User class

@login_manager.unauthorized_handler
# 로그인 안된 사용자가 로그인이 된 사용자만 접근할 수 있는 Request를 요청하는 경우
def unauthorized(): 
    return make_response(jsonify(success=False),401)

app.register_blueprint(blog.blogs,url_prefix='/blog')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')