from flask import Flask
from src import blog_test,blog_test2

app = Flask(__name__)

app.register_blueprint(blog_test.blog_ab,url_prefix='/blog')
app.register_blueprint(blog_test2.blog_ab2,url_prefix='/blog')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')