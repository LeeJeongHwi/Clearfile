from flask import Flask, Blueprint,request,render_template,jsonify,make_response , redirect,url_for

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
        return redirect(url_for('blog.test_blog'))
@blogs.route("/test_blog")
def test_blog():
    return render_template('blog.html')
