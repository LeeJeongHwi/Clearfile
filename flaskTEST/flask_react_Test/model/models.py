import pymysql as mysql

MYSQL_HOST = '117.16.123.11'
MYSQL_CONN = mysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='root',
    passwd='dkimsmu',
    db='powerDB_hour1',
    charset='utf8'
)
def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN