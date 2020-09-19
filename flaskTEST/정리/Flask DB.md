# Flask with DB

### DB 선택

* 변경 여지가 많은 웹 서비스 로깅을 위해선 NoSQL 이용
  * MongoDB 라이브러리로 로그 저장(Scheme가 필요없음)
* 변경 여지가 적은 경우 MySQL 이용
  * 구독으로 얻어진 이메일 주소 정보를 저장

### SQL

* SQLAlchemy
  * DB를 객체로 만들어서 별도의 CRUD 기법을 사용
  * pymysql 보다 성능이..썩 좋진않음 ㅎ
* pymysql로 sql 접근

