from flask_login import UserMixin
from db_model.models import conn_mysqldb

class User(UserMixin):

    def __init__(self,user_id,user_email,blog_id):
        self.user_id = user_id
        self.user_email = user_email
        self.blog_id = blog_id
    def get_id(self):
        return str(self.user_id)
    
    @staticmethod
    def get(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql="SELECT * FROM user_info WHERE USER_ID = '"+str(user_id)+"'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        user = User(user_id=user[0],user_email=user[1],blog_id=user[2])
        return user
    
    @staticmethod
    def find(user_email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql="SELECT * FROM user_info WHERE USER_EMAIL = '"+str(user_email)+"'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        user = User(user_id=user[0],user_email=user[1],blog_id=user[2])
        return user
    
    @staticmethod
    def delete(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "delete from user_info where user_id = %d"%(user_id)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted

    @staticmethod
    def create(user_email,blog_id):
        user=User.find(user_email)
        if user == None:
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql="INSERT INTO user_info (USER_EMAIL,BLOG_ID) VALUES ('%s','%s')"%(str(user_email),str(blog_id))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        else:
            return user
