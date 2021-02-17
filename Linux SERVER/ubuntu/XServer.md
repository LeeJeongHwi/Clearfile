# Starting Xserver in Ubuntu on Docker



### Use GUI Application in Docker Container on Ubuntu

* Development Environment
  * OS - Ubuntu 20.04 LTS
  * Docker - 19.03.13

* Run Docker Container (in Ubuntu CLI)

```ubuntu
$  docker run -it --name [name] -e DISPLAY=$DISPLAY -e USER=$USER -v /tmp/.X11-unix:/tmp/.X11-unix -v /root/.Xauthority:/root/.Xauthority --net host [images:version]
```

X Windows 와 연동할 수 있도록 옵션을 붙여서 수행

* System Link Test in Docker Container

```ubuntu
$ apt-get update
$ apt-get install x11-apps
..
- Success Install..
..
$ xeyes
```

여기서 해당 에러가 발생할 수 있다.

`Error : Can't open dispaly :...`

에러를 해결하기위해 다음과 같이 수행한다.

```ubuntu
$ xhost +local:docker  (In Ubuntu)
```

만약 이래도 처리가 안된다면 Container내에서 다음과 같이 써본다.

```ubuntu
$ export DISPLAY = [접속하고 있는 IP]:0.0
```

![image-20210217135900794](C:\Users\JeongHwi\AppData\Roaming\Typora\typora-user-images\image-20210217135900794.png)

xeyes가 실행됨을 볼 수 있다.



앞으로 나도 ubuntu에는 필요한 것만 설치하고, Docker로 주로 작업을 해야겠다.