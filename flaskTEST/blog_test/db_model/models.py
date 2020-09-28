import pymysql as mysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = mysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='root',
    passwd='rjdnf88as',
    db='test',
    charset='utf8'

)

def conn_mysqldb():
    if not MYSQL_CONN.open: #connection Check
        MYSQL_CONN.ping(reconnect=True) # 재접속 시도
    return MYSQL_CONN