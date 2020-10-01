## 해야될 일

* Container Decoupling

  * Server 관리자만 Docker를 관리
  * Server 관리자 외에는 Docker Container에 접속 (어떤 방식으로..?)
    * `docker exec` 으로 접근하지 말고 바로 ssh 접속으로 인지?

* 볼륨 관리 (Container 내부 데이터 관리)

  * DB는 Persistence를 유지해야하는 특성이 있다. 따라서 컨테이너 내부 볼륨과 호스트 볼륨이랑 연동시킴
  * 볼륨 구성

  > ~/Dockers/flask : 플라스크 소스코드
  >
  > Docker volume : 볼륨 관리

* 외부접속? How to?

  * 포트포워딩 문제였음
  * 외부IP : Port 를 했을 때 포워딩 규칙이 있는 것들에만 접속이 가능함.. 따라서
  * mysql -h [ip] -u root -p 를 하면 잘 들어가짐 ;)
  * portainer도 마찬가지  > [ip]:9000
