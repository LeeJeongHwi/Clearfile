# Docker

## Docker?

* Linux 컨테이너를 만들고 사용할 수 있도록 하는 컨테이너화 기술
  * 하나의 프로세스!
* 컨테이너를 매우 가벼운 모듈식 가상 머신 처럼 다룰 수 있음
  * 구축, 배포, 복사하고 한 환경에서 다른 환경으로 이동하는 등 유연하게 사용 가능
* Immutable, Stateless, Scalable
* Linux Base
  * 현재는 Windows 버전도 나옴



### Container?

* 시스템의 나머지 부분과 격리된 프로세스 세트
  * 개발 단계에서 테스트, 프로덕션에 이르기까지 이식성, 일관성을 유지할 수 있음
  * 전통적인 테스트 환경을 복제하는 개발 파이프라인보다 훨씬 더 빠른 배포를 실현 할 수 있음

![image-20200919170002345](./figure/container)


* 사용하는 이유
  * 노트북에서 특정하게 설정된 환경을 사용하여 작업
  * 다른 개발자들의 구성은 약간 다를 수 있음
  * 이때 환경을 재구축하는 부가적인 작업 없이 가능한 로컬에서 특정하게 설정된 환경을 작동시킴
* 특징
  * 동일한 운영 체제 커널을 공유
  * 시스템의 나머지 부분으로부터 애플리케이션 프로세스를 격리
    * Ubuntu 18.04 container / Ubuntu 20.04 container / x64 Windows Container.. 이런 식으로
  * 기본 시스템과 호환이 되어야함
* 장점
  * 모듈성
  * 롤백
  * 신속한 배포
  * 계층 및 이미지 버전 제어

> 우리는 DB(Maria or MySQL) 컨테이너, Web Server 컨테이너, Deap Learning 컨테이너로 구성을 할 계획이다.



### Docker Terms

* Contrainer
  * 논리적으로 쪼개져있는 영역
  * 컨테이너는 "하나의 프로세스" 라고 생각하면 된다.
  * VM과 다른 점
    * VM은 별도의 OS가 된다 (PC 1개가 2개로 쪼개지는 것)
    * Docker는 1개의 PC에서 여러개의 프로세스로 나눠서 쓰는것
* Image
  * 구성된 프로세스
  * Image 한개가 container 한개다 라고 생각하면됨
  * 다른 서버에서 쓰고싶으면 image로 복사해놓는다.
  * container를 바탕으로 해서 떠놓은 것
  * Image Build(Make) : Dockerfile
    * build 해 놓은 것을 다른 서버에 image를 올려서 사용한다는 뜻?
    * 일일히 설치 할 필요없이!
  * Image ship(share)

* Pull
  * image를 받는 것

> Image는 서비스 운영에 필요한 서버 프로그램, 소스 코드, 컴파일 된 실행 파일을 **묶은 형태**
>
> Container는 그 Image는 실행 시킨 **프로세스** 라고 생각하면 편하다

### Docker Principle

* Namespace
  * PID, UID .. 등등 분리

* docker0 NIC (Network interface controller)
  * Network도 분리가능



### Portainer

* docker의 이미지,컨테이너,네트워크 등을 쉽게 관리할 수 있게 도와주는 GUI Web 서비스



## 명령어

* docker ps
  
  * 실행 중에 있는 Container
* docker ps -a
  
  * 실행 내역?
* docker system df
  
  * 디스크 사용량을 나타내는 것
* docker pull [image]
  
  * 이미지 다운로드
* docker image ls
  
  * image 목록
* docker container run --name [name] -d -p [명령]
  * -d : detach (background으로 돌리겠다)
  * -p : port 설정
  * (nginx 는 기본적으로 80 포트로 설정되어있따.)
  * -it : CLI 형태로 구동 가능?
  * 처음 Container를 올릴 때 사용
  * ctrl+PQ --> detach
  
  > links 옵션은 
* docker start [name]
  * 전에 생성된 컨테이너 실행
  * restart 는 강제 재실행
* docker stop [name]
  
  * 컨테이너 중지
* docker container attach [name]
  
  * 실행 중인 도커 컨테이너 안으로 들어감
* docker rm [name]
  
  * 컨테이너 삭제
* docker exec ...
  
  * 하나의 명령만 실행할 때 (컨테이너가 떠있는 경우에만!)
* docker rename [name] [ch_name]
  
  * 이름 변경
* docker cp [container-name]:[path] [client-path]
  docker cp [client-file] [container-name]:[path]
  
  * file 복사 (컨테이너 -> 로컬 , 로컬 -> 컨테이너)  
* docker run -v [local-path]:[container-path]
  
  * 디렉토리 공유
* docker commit [Container] [ImageName]:[tag]
  * container to Image (작업중인 container를 image로 생성)
  * 주의할 점은 볼륨을 host와 공유하지 않으면 commit을 해도 변화된 데이터베이스는 저장되지 않는다.
    * run 시킬 때 -v로 공유볼륨을 지정해줘야함

>* mariaDB server 의 경우
>
>`-v [local-path]:/var/lib/mysql ` // docker-hub mariaDB official 에 올라온 path

* docker build -t -f ...
  * Dockerfile을 실행시키기 위한 명령어
  * -t 이미지 파일에 붙일 태그생성
  * -f 참조할 dockerfile 명
  * 뒤에 꼭 "."를 붙이자..! (도커파일이 현재 실행되고 있는 디렉토리에 있다는 뜻!)

>만약 run 중에 까먹고 -v -p 등 옵션을 설정해주지 않고 다른걸 이미 설치해버린 상태라면 commit 후에 다시 run 할 때 설정해주면 된다.

## Dockerfile

* 이미지를 만드는데 사용하는 파일

#### 명령어

* FROM
  * 베이스이미지 지정
* MAINTAINER
  * Dockerfile 관리자 정보
* COPY
  * 파일이나 디렉토리를 이미지로 복사 (소스를 복사하는데 사용)
  * COPY [localPath] [Container Path]
* ADD
  * COPY와 비슷한 일을 함
* RUN
  * 명령어를 그대로 실행한다. 내부적으로 /bin/sh -c 뒤에 명령어를 실행하는 방식
* CMD
  * 도커 컨테이너가 실행되었을 때 명령어를 정의
  * 빌드할 때에는 실행 X
  * 좀 더 공부가 필요함
* WORKDIR
  * RUN, CMD, ADD, COPY가 이루어질 디렉토리 설정
  * 명령어는 한 줄 한 줄마다 초기화되기 때문임
* EXPOSE
  * 컨테이너가 실행되었을 때 요청을 기다리고 있는(Listen) 포트 , 여러개의 포트 지정
* VOLUME
  * 컨테이너 외부에 파일 시스템을 마운트 할 때 사용
  * `VOLUMNE [Container Path]`
  * `sudo docker run -v [local path]:[container path]`
* ENV
  * 환경변수 설정 
  * `ENV [환경변수] [값]`

> 도커파일 작성하는 것은 꽤 어려움..

## Docker Compose

* 하나의 이미지엔 하나의 앱만 넣고 여러 컨테이너를 조합하여 서비스를 구축하는 방법이 좋다
* 여러개의 컨테이너를 실행 시키는 패턴
  * Docker-Compose 이용
* 방향

![image-20200923171717864](./figure/container 구상도)

* 예상 구상도는 다음과 같다

  * DB Server , Web Server (Front,Back) , ML/DL Server

  * 각각의 컨테이너에서 작업을 하고 Docker-Compose로 3개를 동시에 실행시키는 것

  * 따라서 DB를 교체시에 DB Container만 수정하면 되도록 구현하는 것

