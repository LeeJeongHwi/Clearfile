# Flask 예제 테스트

* 링크 : https://kkamikoon.tistory.com/161?category=825129



## Flask

* Flask는 Python 웹 프레임워크 중 하나이다.
* Django는 Full stack Web Framework에 반해, Flask는 가볍다. (매우 단순 가볍)
  * Django가 기능은 훨씬 뛰어남 (복잡)
* URL Routing, Template, Cookie, Debugger 및 개발 서버 등 기본 기능만 제공
* ORM(Object Relational Mapping) 기능이 없음
  * 데이터베이스 연결, 양식 처리, 보안, 인증 모두 개발자가 직접 처리
* 단순한 REST API서버는 Flask가 더 효율적



### 디렉토리 폴더 구성

Flask에서 정의되어 있는 디렉토리 구조이기 때문에 따라야한다.

* project_name/templates - html 파일이 들어갈 위치
  * ```render_template()``` 를 수행할 시 templates 폴더에 있는 html 파일들을 보여준다.
* project_name/static - html 파일 내에 이미지,js,css 링크를 참조하는 파일들
* flask 메인 py 파일은 project_name/ 에 위치해야한다.

### 라우팅 (Routing)

* 적절한 목적지를 찾아주는 기능

* URL을 해당 URL에 맞는 기능과 연결

* '/' 로 시작해야한다.

* ```python
  @app.route('/hello')
  def hello():
      return {datas}
  ```

  * app.route()에 밑에 선언된 함수를 호출하게 한 것이다 (@ 데코레이터)
  * return으로 restAPI, 웹페이지 등등.. return

* https - 포트번호 443
  http - 포트번호 80
  현재 상용되는 웹사이트에서는 포트를 자동적으로 붙여준다

* 데이터 전달

  * ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return "<h1>Hello World!"
    
    @app.route('/test/<username>')
    def get_progilfe(username):
        return "profile"+username
    
    if __name__ == '__main__':
        app.run(host="localhost",port="8080")
    ```

  * <> 내에 변수 이름을 넣으면 들어가는 값을 인자로 넣어 처리해준다.

  * type 도 지정가능

  * `@app.route("/message/<int:value>/")`

#### 데코레이터

* 중첩함수 (Nested Function)

  * Local Function - 로컬 변수처럼 함수 안에서만 사용 가능한 원리와 동일

* First Class Function

  * 함수 자체를 변수에 저장 가능
  * 함수의 인자에 다른 함수를 인수로 전달 가능
  * 함수의 반환 값으로 함수를 전달 가능

  > 파이썬은 객체로 되어있어 first-class 함수로 사용 가능

* Closure Function

  * 외부 함수가 소멸되더라도, 외부 함수 안에 있는 로컬 변수 값과 로컬 함수를 사용할 수 있는 기법
  * 제공해야할 기능이 적은 경우 closure를 사용
  * 제공해야될 기능이 많은 경우 Class를 사용하여 구현

* **Decorator**

  * 함수 앞 뒤에 기능을 추가해서 손쉽게 함수를 활용할 수 있는 기법

  * Closure Function을 활용

    * 데코레이터 아래에 있는 함수를 인자로 준다!

  * 유효성체크 ,Type Check할때 데코레이터를 쓰면 쉽게 적용 가능

  * ```python
    @decorator
    def hello():
        return "hello"
    
    hello()
    ```

### 웹 서버 구동

* 서버로 구동한 IP와 포트를 옵션으로 넣어줄 수 있음

* app.run() 함수로 서버 구동

* ```python
  app.run(host=웹주소,port=포트,debug=T/F)dd
  ```

* 웹 서버는 정적인 HTML를 반환

  * Request에 따른 정적인 데이터 반환

* WAS 프레임워크

  * 웹서버가 동적으로 데이터를 반환하도록 하기위한 프레임워크
  * Flask, Django, node.js , rails.....



### REST API

#### HTTP(Hypertext Transfer Protocol)

* Client --> HTTP Request --> Server
* Server --> HTTP Response --> Client

* Client 에서 요청 , Server에서 응답

* ```python
  GET / HTTP/1.1
  GET : HTTP Method
  /   : Path (routing 경로)
  HTTP/1.1 : HTTP 버전
  Host : ..
  Connection : Keep alive # 한번 연결해 놓고 계속 사용
  ```

* HTTP는 1회성 (연결 과정작업을 계속 해야함)

  * 한번 연결 해놓고 연결 과정 작업을 계속 굳이 하지말아라!
    * Connection

* GET

  * 정보를 가져오는 메소드

* 입력창에 데이터를 넣고, Submit을 하고 그거에 대한 일종의 **결과값**을 서버에서 return 받을 때, 이때 REST API방식을 사용한다 라고 함!

#### REST

* REPressentational State Transfer
* 자원의 표현에 의한 상태 전달
* HTTP URI를 통해 자원을 명시하고, HTTP Method를 통해 자원에 대한 CRUD Opertaion 적용
  * Create : POST
  * Read : GET
  * Update : PUT
  * Delete : DELETE

#### REST API

* REST 기반으로 서비스 API 를 구현한 것
* 마이크로 서비스, OpenAPI 등에서 많이 사용

#### Flask with REST API

* 특정한 URI를 요청 --> JSON 형식으로 데이터를 반환
* 

