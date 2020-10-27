# Scheduler

**Scheduler 정의**

* 특정시간마다 특정 함수를 실행시키도록 하는 도구



> 참조 : https://apscheduler.readthedocs.io/en/latest/index.html   (공식 Document)

### apscheduler

**설치 : ** `pip install apscheduler`

#### 구성

* triggers
  * Scheduling Logic을 포함하고있는 것
  * 각각의 job은 다음에 실행시킬 시기를 결정하는 고유한 trigger를 갖고있음
* job stores
  * 예약된 작업을 보관하는 저장소
  * 작업 저장소는 작업 데이터를 메모리에 저장하지 않고 백엔드에서 작업을 저장,로드,업데이트,검색하는 **중간 관리자 역할**
* executors
  * 작업의 실행을 처리하는 곳
  * 작업 완료 시 executors 가 Scheduler 알림, 그리고 적절한 이벤트 발생시킴
* schedulers
  * 위 세개를 하나로 묶음 --> 얘만 실행됨
  * 오직 하나의 scheduler만 실행 가능함
  * scheduler는 위 3가지를 다룰 수 있는 적절한 인터페이스 제공



#### Scheduler 종류

* BlockingScheduler : 단일 스케쥴러
* BackgroundScheduler : 다중 스케쥴러

> 그 외 다른 scheduler로 있지만 사용되지 않을 것으로 판단



#### 실행 방식

* Cron : 특정 시간에 정기적으로 작업을 실행
* Interval : 일정 주기로 실행
* Date : 특정 날짜로 한 번만! 실행 (= Cron)



### Scheduler를 사용해야 될 파트

일단 실시간 서비스를 구축하기 위해선 SocketIO에 대해서 공부해야한다.

* 1시간 마다 전력데이터를 가져와서 DB에 저장하고 그 데이터를 Front에 띄운다.
* 24시간 마다 다음 예측에 필요할 데이터를 DB로부터 가져와서 TF Server에 전송한다.
  * 전송 후 예측 된 값을 DB에 저장
  * 

