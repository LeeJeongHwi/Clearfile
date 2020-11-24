from model.models import conn_mysqldb

class mapinfo():
    def __init__(self,id,name,type_,lat,long,detail,code):
        self.id = id
        self.name = name
        self.type_ = type_
        self.lat = lat
        self.long = long
        self.detail = detail
        self.code = code
    
    @staticmethod
    def get():
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT id,name,latitude,longitude,detail_addr FROM building"
        db_cursor.execute(sql)
        datas = db_cursor.fetchall()
        db_cursor.close()
        print(datas)
        if not datas:
            return None
        return datas