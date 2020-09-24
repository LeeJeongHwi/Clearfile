# Docker-Compose

* 하나의 이미지엔 하나의 앱만 넣고 여러 컨테이너를 조합하여 서비스를 구축하는 방법이 좋다
* 여러개의 컨테이너를 실행 시키는 패턴
  * Docker-Compose 이용
* 방향

![image-20200924195531319](./figure/container 구상도)

* 예상 구상도는 다음과 같다

  * DB Server , Web Server (Front,Back) , ML/DL Server

  * 각각의 컨테이너에서 작업을 하고 Docker-Compose로 3개를 동시에 실행시키는 것

  * 따라서 DB를 교체시에 DB Container만 수정하면 되도록 구현하는 것

#### 명령어

* `docker-compose up`
  * -d : 서비스 실행 후 콘솔로 나오기
  * --force-recreate : 컨테이너를 지우고 새로 만들기
  * --build : 서비스 시작 전 이미지를 새로 만들기
* `docker-compose down`
  * --volume : 볼륨까지 삭제
* `docker-compose exec`
  * 실행 중인 컨테이너에서 명령어를 실행
* `docker-compose logs`
  * 서비스의 로그를 확인

## DockerFile 구성

### uWSGI + flask 

```dockerfile
FROM python:3.7.9

ADD . /flask
WORKDIR /flask
VOLUME /flask
RUN python -m pip install --upgrade pip
RUN pip3 install Flask
RUN pip3 install uwsgi

CMD uwsgi uwsgi.ini
```

#### uwsgi.ini

```ini
[uwsgi]
chdir=/flask/src
socket=:5000
wsgi-file=/flask/src/run.py
callable=app
master=true
processes=4
threads=2
```

### nginx

```dockerfile
FROM nginx:1.17.4
COPY default.conf /etc/nginx/conf.d/default.conf
CMD ["nginx","-g","daemon off;"]
```

#### Default.conf

```conf
upstream flask_uwsgi{
    server flask:5000;
}

server{
    listen 80;
    server_name 127.0.0.1;
    location /{
        include uwsgi_params;
        uwsgi_pass flask_uwsgi;
    }
}
```

### Mariadb

* Mariadb 는 pull로 image를 받고 docker-compose.yml에서 image로 쓴다.



## Docker-compose.yml

* `docker-compose up` 할 때 실행하는 파일

```yml
version: '3'

volumes:
    mariadb_dev:

services:
    db:
        container_name: db
        image: "mariadb:latest"
        ports:
         - "8080:8080"
        volumes:
         - mariadb_dev:/var/lib/mysql
        environment:
         MYSQL_ROOT_PASSWORD: dkimsmu
        restart: always
        networks:
        - backend
    flask:
        container_name: flask
        image: "flask:test"
        ports:
        - "5000:5000"
        networks:
        - backend
        volumes:
        - ./flask:/flask
        depends_on:
        - db
        links:
        - db
    nginx:
        container_name : nginx
        image: "nginx:test"
        ports:
         - "80:80"
        networks:
         - backend
        depends_on:
        - flask

networks:
    backend:
        driver: bridge
```

* 실행순서 : DB -> Flask+uwsgi -> nginx

#### 실행결과

![image-20200924172735099](./figure/result_db_flask)

* 첫번째 사진은 현재 docker에 올라가있는(실행 중인) container들을 보여준 것입니다.
* 두번째 사진은 Server컴퓨터에서 실행시킨 flask server를 로컬컴퓨터(작업 컴퓨터)에서 접속한 화면입니다.
* 세번째 사진은 flask 컨테이너에서 db 컨테이너에게 ping을 보내서 현재 네트워크 연결이 되어있음을 의미합니다.

![image-20200924195343907](./figure/docker_vsTest)

* 해당 사진은 Visual studio code 내에서 Flask Container 속에 있는 html파일을 수정한 결과입니다. 

### DB -> Flask

![image-20200924203614066](./figure/mariadbFlask)

* 해당 Flask Container 에서 DB container에 Create Table을 반영시킨 결과입니다.

> 결론

* 현재 MariaDB + (Flask + uWSGI) + Nginx 을 Docker-compose로 연동시켰습니다
* ML/DL Server( Tensorflow serving ) 는 아직 컨테이너를 올리지는 못한 상태입니다.
* 지금부터 웹 서버 개발은 시작해도 가능할 것 같습니다.
  하지만 문제점은 노트북 상에서 (docker container) Flask Server를 열었을 때 접속할 수 없습니다.
  * 이 문제점은.. 어떤 문제인지 잘 모르겠습니다
  * 저의 생각은 집에서는 외부 IP로 접속을 해야하므로 `[외부IP]:80` 을 했을 때 접속이 되어야 한다고 생각하는데, 되지 않습니다..
  * 이 문제가 해결되면 집에서도 충분히 개발이 가능할 것 같습니다.
  * 일단은 집에서도 SSH 접속은 가능합니다.
    * MobaXterm으로 SSH 접속 후 Local 에서 개발한 파일 (React나 Flask)를 Server 컴퓨터내로 전송하면 일단은 되긴 됩니다!