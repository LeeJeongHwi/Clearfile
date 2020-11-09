import time
from model.models import conn_mysqldb
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BackgroundScheduler()
sched.start()

conn = conn_mysqldb()
def insertFunc():
    cursor = conn.cursor()
    sql = "Select * from map_info where id = %d"%(2)
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    print(data)

sched.add_job(insertFunc, "interval",seconds = 5)

try:
    while True:
        print("Running Main Process..")
        time.sleep(1)

except:
    sched.shutdown()

