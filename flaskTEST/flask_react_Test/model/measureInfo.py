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
        select lTBL.id, lTBL.title, mTBL.hour, mTBL.1hour_use, lTBL.type
        from
        (select id, date, HOUR(time) AS 'hour', round(sum(measure_power),2) as '1hour_use',
         count(measure_power) as count_Measure from measureTBL GROUP BY DATE(date), 
        Hour(date_sub(time, interval 15 minute)) having count_Measure>=4) as mTBL
        natural join 
        (select id,title,type from locationTBL) as lTBL
        where lTBL.id = "%s" order by mTBL.hour;
        """%(id)
        db_cursor.execute(sql)
        datas = db_cursor.fetchall()
        db_cursor.close()
        print(datas)
        if not datas:
            return None
        return datas