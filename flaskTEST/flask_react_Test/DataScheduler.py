import time
from model.models import conn_mysqldb
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BackgroundScheduler()
sched.start()

conn = conn_mysqldb()
t = 0
def insertFunc():
    global t
    cursor = conn.cursor()
    t+=1
    sql = "Insert into map_info values(%d,'TEST_%d','%d','%d')"%(0,t,t*10,t*100)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    print("Commit Complete, TEST_%d %d %d"%(t,t*10,t*100))

sched.add_job(insertFunc, "cron",minutes = 15)

try:
    while True:
        print("Running Main Process..")
        time.sleep(1)

except:
    sched.shutdown()

"""
이 스케쥴러는 실시간 전력 데이터를 받아와서 DB에 저장하는 스케쥴러
*  1시간마다 실시간 전력 데이터를 어딘가로부터 받아와 우리 DB 서버에 저장


다른 스케쥴러는 Tensorflow Serving 용으로 만들어야함
* Tensorflow Serving 에서 사용량을 보냄 --> 예측 --> 받아서 저장 (24시간)
"""
