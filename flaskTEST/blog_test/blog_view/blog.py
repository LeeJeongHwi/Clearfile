from flask import Flask, Blueprint,request,render_template,jsonify,make_response , redirect,url_for
from flask_login import login_user,current_user,logout_user
from blog_control.user_mgmt import User
import datetime
#redirect : 다른 라우팅 경로로 변경해주는 역할
#url_for : blog.test_blog... 라우팅을 전달
blogs = Blueprint('blog',__name__)

@blogs.route("/set_email",methods=['POST',"GET"])
def set_email():
    if request.method=='GET':
        print('set_meail', request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))
    elif request.method=='POST':
        print(request.headers) # Content-Type이 Json이면 request.get_json()를 사용해야한다.
        print("set_email",request.form['user_email'])
        user = User.create(request.form['user_email'],'A')
        login_user(user,remember=True,duration=(datetime.timedelta(minutes=3)))
        return redirect(url_for('blog.test_blog'))

@blogs.route("/test_blog")
def test_blog():
    if current_user.is_authenticated: #current_user는 login_user.user_loader에서 User를 불러옴 
        print("CurrentUser : ",current_user.user_email)
        return render_template('blog.html',user_email=current_user.user_email)
    else:
        return render_template('blog.html')

@blogs.route("/logout")
def logout():
    User.delete(current_user.user_id)
    logout_user()
    return redirect(url_for('blog.test_blog'))
