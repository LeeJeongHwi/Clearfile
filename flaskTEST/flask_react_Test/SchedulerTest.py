from apscheduler.schedulers.background import BackgroundScheduler
import time
sched = BackgroundScheduler()

@sched.scheduled_job('interval', seconds =5, id ='test_1')
def job1():
    print(f"job1 : {time.strftime('%H:%M:%S')}")

@sched.scheduled_job("cron",hour="17",minute="45",id='test_2')
def job2():
    print(f"job2 : {time.strftime('%H:%M:%S')}")


sched.add_job(job2,"cron",second='0',id='test_3')

print("Sched Before")
sched.start()
print("sched after~")

while True:
    time.sleep(1)