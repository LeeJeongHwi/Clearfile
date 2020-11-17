from model.models import conn_mysqldb

class mapinfo():
    def __init__(self,id,name,type_,lat,long):
        self.id = id
        self.name = name
        self.type_ = type_
        self.lat = lat
        self.long = long
    
    @staticmethod
    def get(id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM locationTBL WHERE id = '%s';" %(id)
        db_cursor.execute(sql)
        datas = db_cursor.fetchone()
        db_cursor.close()
        print(datas)
        if not datas:
            return None
        return datas