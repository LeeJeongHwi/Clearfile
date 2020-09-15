## Flask 

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
  * Create : POST - 데이터 추가
  * Read : GET - 데이터 조회
  * Update : PUT - 데이터 업데이트(정보를 통째로 갈아치움)
  * Delete : DELETE - 데이터 제거
* 각 요청이 어떤 동작이나 정보를 위한 것인지를 그 요청의 모습 자체로 추론 가능
* 자원을 구조와 함께 나타내는 이런 형태의 구분자를 URI라고함

#### REST API

* REST 기반으로 서비스 API 를 구현한 것
* 마이크로 서비스, OpenAPI 등에서 많이 사용

#### Flask with REST API

* 특정한 URI를 요청 --> JSON 형식으로 데이터를 반환

* 웹주소(URI) 요청에 대한 응답(Response)를 JSON 형식으로 작성

* Flask에서는 Dict(사전) 데이터를 응답 데이터로 만들고, 이를 jsonify() 메서드를 활용해서 JSON 응답 데이터를 만들 수 있음

  * JSON Format

    ```json
    {
        "name":"LEEJEONGHWI",
        "age" :24,
        "use_lang" : [
         	{
                "Python":5.0 //능력치
                "C++" : 3.5
            }   
        ]
    }
    ```

* jsonify

  * Json을 프론트 엔드로 보낸다.

* request

  * 파라미터 값을 받기 위해 사용

  * `username = request.args.get('user_name')` : 'get' 방식으로 요청된 파라미터는 주소에 붙어져서 전송함

  * URL?파라미터이름=파라미터값
    `http://localhost:8080/login?user_name=jeonghwi`

    여러개의 파라미터

    `http://localhost:8080/login?user_name=jeonghwi&pw=111&email=wjdgnl97@gmail.com`

    