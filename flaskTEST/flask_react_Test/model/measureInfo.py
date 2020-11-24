from model.models import conn_mysqldb

class meausreInfo():
    def __init__(self,id,title,hour,power,types):
        self.id = id
        self.title = title
        self.hour = hour
        self.power = power
        self.types = types
    @staticmethod
    def get(id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = """
        select building.id,building.name,building.detail_addr, building.code, measure_power.date, hour(measure_power.time) AS hour, measure_power.measure_power
        from measure_power INNER JOIN building 
        ON (measure_power.id = building.id) 
        WHERE measure_power.id = %s and measure_power.date = "2017-01-06";
        """%(id)
        db_cursor.execute(sql)
        datas = db_cursor.fetchall()
        db_cursor.close()
        print(datas)
        if not datas:
            return None
        return datas