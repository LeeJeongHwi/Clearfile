from flask import Flask

app = Flask(__name__)

# from app.main.index import main as main
# app.register_blueprint(main) # 위에서 추가한 파일을 연동해주는 역할

from .test.test import test as test
app.register_blueprint(test)