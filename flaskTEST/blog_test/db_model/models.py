import pymysql as mysql

class Database():
    def __init__(self):
        self.db = mysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd ='rjdnf88as',
            db='test',
            charset='utf8'
        )