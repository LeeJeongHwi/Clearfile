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