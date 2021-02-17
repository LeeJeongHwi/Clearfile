# 패키지 버전 관리

참조 : [Ubuntu에서 Python 버전을 변경하는 방법](https://codechacha.com/ko/change-python-version/)

#### 목적

* Ubuntu를 처음 설치하면 python은 2.7 / 3.8이 자동으로 설치됨, 하지만 기본 실행 버전은 python2 임

  > python3.8은 `python3` 으로 입력해야함

* 파이썬, 자바 등 버전을 여러개를 왔다갔다 쓰는 경우가 생길 때 실행 기본 버전 설정을 해주기 위함



#### 라이브러리

##### `update-alternatives`

* 심볼릭 링크를 관리해주는 리눅스 프로그램

내 컴퓨터 WSL2 의 경우 다음과 같이 설정되어 있다.

```ubuntu
$/usr/bin# ls | grep python

dh_python2
python
python2
python2.7
python3
python3.8
```

그리고 현재 python은 `/usr/bin/python2.7` 을 가리키고 있다.

#### `update-alternatives`로 파이썬 버전 등록 및 변경

```ubuntu
$ sudo update-alternatives --config python
```

* python의 버전을 변경하는 옵션

* 처음인 경우 등록이 되어있지 않아서 등록을 해주어야 한다.

```ubuntu
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2
```

* 다시 `--config` 옵션으로 확인하면 다음과 같이 설정되어 있다. 바꿀 버전의 번호를 입력으로 준다.

```ubuntu
$ sudo update-alternatives --config python
There are 2 choices for the alternative python (providing /usr/bin/python).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3.8   2         auto mode
  1            /usr/bin/python3.8   1         manual mode
  2            /usr/bin/python2.7   2         manual mode

Press <enter> to keep the current choice[*], or type selection number: 1
```

그리고 다시 CLI에 `python`을 입력해본다.

```ubuntu
$ python
Python 3.8.2 (default, Jul 16 2020, 14:00:26)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

* 위와 같이 3.8 로 설정된 python IDLE이 나온다.



#### 주의할 점

파이썬 패키지 설치를 위한 pip는 **`pip3`** 로 설정해야함

#### `$ apt-get install python3-pip`





