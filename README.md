# Study-Repo

### :file_folder: 폴더구성

* repo/flaskTEST : 플라스크 공부 관련 내용

* repo/LinuxSERVER/Docker : 도커 공부 관련 내용



# :calendar: 개발일지

## 2020.09.29

* Container (SQL DB, Portainer) 에 개별적으로 접근 가능하도록 port fowarding 설정
  * `mysql -h [ip] -u root -p` : Server컴퓨터 내 --> DB container

* FlaskTEST update
  * MVC패턴 기본적인 틀 작성

## 2020.09.25

* 이제부터 Flask 70, Docker 30에 힘을 쓰자
* Flask Blog WebPage(인터넷 강의) 실습
* Docker 구성을 어떻게 해야할지 고민

## 2020.09.24

* 도커파일 python 작성하고 nginx+ flask,uwsgi + MariaDB 연결
* 자세한 결과는 DockerCompose.md 파일 참조

#### 문제점

* 여전히 노트북 상에서 해당 서버컨테이너 내에서 열은 페이지에는 접속이 되지 않음

## 2020.09.22

* Dockerfile, Docker 명령어에 대한 공부
  * 주로 Docker commit  Volume에 관해 좀 더 공부함
* 내부망으로는 Container의 서버에 접근이 가능한데, 외부망으로는 불가함 --> 왜지?

> Dockerfile로 각 컨테이너마다 Ubuntu를 설치해야하나?
>
> 아니면 Webserver만 Ubuntu를 설치하고 그 위에 톰캣, Flask를 설치할까?
>
> Front Container , Back Container를 따로잡아야 할까?
>
> ML/DL 환경은 어떻게 구성할까?
>
> 가장 큰 문제는 MobaXterm으로는 ssh 접속이 가능한데,로컬이 그 내에 있는 Docker에 있는 Container로 접근이 안된다는 것이다.

#### 해야될 일 

* Docker 환경 구성
  * 현재 DB Container는 생성함
  * Webserver 진행 중
* 집에서는 Flask 공부할 것!
  * Flask의 Controller,Model 구성, View는 Front 단에서 구성이므로 가볍게 구성하기
  * Flask만의 구성법을 찾아보자
    * Github의 오픈소스를 많이 읽어보자!

## 2020.09.21

* Docker 설치 및 MySQL 서버 컨테이너 생성 , 그 외 및 Docker 개념 공부
* Flask
  * Login 파트
  * MVC 패턴에 대해서 좀 더 공부해야할 듯함

#### 해야될 일

* docker 공부 (서버가 우선적으로 구축이 되어야하기 때문..)
  * 노트북으로 내부 Container 접근하는 방법 찾기.. (portainer 페이지를 접속할 수 없음..내부망 이외에는)
* Flask MVC template 생각해보기

## 2020.09.19

* 서버 컴퓨터 구축
  * 핸드폰 셀룰러 테더링으로 노트북의 와이파이를 잡아서 접속 시도 --> 성공!!!
  * 현재 외부 ip 주소로 집 노트북이나 컴퓨터로 접속 가능함
    * 접근 아이피를 설정해서 특정 ip만 접속할 수 있도록 만드는 것도 좋을듯
  * 어제 문제점
    * port 가 22가 아닌 다른 포트를 사용해서 해결함
* 결과 (집에서 연구실 서버에 접속 결과)
  <img src="C:/Program Files/Typora/flaskTEST/정리/successlogin.png">

#### 해야될 일

* Docker로 서버 구성?
* MVC 패턴을 적용한 Flask Server template

## 2020.09.18

* Linux Ubuntu server 생성
  * ssh 할때 port 22도 허용을 해줘야 포트포워딩 했을 때 접속이 가능
  * 연구실에 있는 PC (공유기가 연결되어있는 상태) 로 접속 성공

> 어떤 문젠지는 모르겠지만 노트북으로 와이파이로 접근 시에 접속이 안되는 현상..



