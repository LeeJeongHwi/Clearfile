import time
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()
sched.start()
try:
    while True:
        print("Running Main Process..")
        time.sleep(1)

except:
    sched.shutdown()