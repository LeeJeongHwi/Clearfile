# DockerFile 구성

```dockerfile
FROM ubuntu:18.04
MAINTAINER LeeJeongHwi@<wjdgnl97@gmail.com>
RUN mkdir /opt/flask/
WORKDIR /opt/flask
VOLUME /opt/flask

```

https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh