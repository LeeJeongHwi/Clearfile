import pymysql as mysql

MYSQL_HOST = ''
MYSQL_CONN = mysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='root',
    passwd='',
    db='powerDB_hour1',
    charset='utf8'
)
def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN