from model.models import conn_mysqldb

class mapinfo():
    def __init__(self,id,name,lat,long):
        self.id = id
        self.name = name
        self.lat = lat
        self.long = long
    
    @staticmethod
    def get(id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM map_info WHERE id = %d;" %(id)
        db_cursor.execute(sql)
        datas = db_cursor.fetchone()
        print(datas)
        if not datas:
            return None
        return datas