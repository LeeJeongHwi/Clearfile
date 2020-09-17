# Flask and Vue

* 정적 + 동적 = Front-end 기술
* Back-end 는 RestAPI를 제공, Front-end 와 통신하고 데이터를 주는 것이 주된 요인

### CDN(Contents Delivery Network)

* 지리적, 물리적으로 떨어져 있는 사용자가 Server에 요청할때, 사용자와 가까운 곳에 위치한 Cache Server에 해당 컨텐츠를 저장해놓고, 메인 서버가 아닌 Cache Server가 응답해주는 기술

### HTTP 요청 메서드 (request method)

* GET POST PUT DELETE -> 그중 GET,POST를 주로 사용

## Vue

### Axios

* 웹과 다른 시스템 간에 통신이 가능하도록 함 (HTTP 프로토콜 사용)
* flask Rest API 호출

### Vue + Axios

* HTML

  ```html
  <!-- Vue 영역 -->
  <div id='app'>
      <button v-on:click='axios_test'> # 클릭시 axios_test 함수를 불러온다
          GET TEST
      </button>
  </div>
  <script>
          const app = new Vue({
              el:"#app",
              methods : {
                  axios_test(){
                      axios("http://localhost:8080/test",{
                          method: "get",
                      }).then((response) => {
                          console.log(response);
                      }).catch((error) =>{
                          console.log(error);
                      });
                  },
              },
          });
      </script>
  ```

  Python

  ```python
  from flask import Flask,render_template,make_response,request,jsonify
  from flask_cors import CORS
  app= Flask(__name__)
  CORS(app)
  
  @app.route('/test',methods=['GET'])
  def test():
      return make_response(jsonify(success=True),200)
  
  if __name__ == "__main__":
      app.run('0.0.0.0',port='8080')
  ```

  * 버튼 클릭시 axion_test 함수를 불러옴!



### CORS

* 웹페이지는 다른 웹페이지를 참조할 수 있따.

* 다른 서버에 있는 데이터,파일도 모두 가져올 수 있음!

* `<sciprt></script>`로 둘러싼 코드 안에서 다른 서버로 접속하는 http request를 호출하면 에러가 발생함

  * Same Origin Policy
  * script안에 둘러 쌓인 코드는 동일한 서버 내에서만 http request를 호출할 수 있따.

* 안에서도 다른 사이트의 데이터 요청을 지원해야 한다라는 요구가 생겨서 CORS라는 가이드가 마련됨

* Flask 내에 코드

  ```python
  app = Flask(__name__)
  CORS(app)
  ```

  * Header 부분에 `Access-Control-Allow-Origin: *` 가 추가된다.

#### make_response()

* status 코드를 명확하게 써서 넘기는 경우
  * 200인 경우 성공
  * 400,401,403,404,500 .. 등등 상태 코드가 있음
  * http status code < 로만 쳐도 설명이 나옴!



### REST API method

```python
if request.method == 'POST':
    data = request.get_json() # 파라미터들을 dict 형태로 불러옴
    ...
if request.method == 'GET':
    user = request.args.get(파라미터)
    ...
if request.method == 'PUT(or DELETE)'
```



#### Form tag

```html
<form method='post(or get)' action='~.html'>
    id : <input>
    pw : <input>
</form>
```

* GET 방식은 파라미터 값이 ?,& .. 등등을 이용해서 주소창에 파라미터 값이 붙어져서 전송
* POST 방식은 주소창은 바뀌지않고, Body 부분에 input으로 넘겨진 데이터가 들어간다.(사용자는 직접 확인 X)
  * ID,PW 등 중요한 정보를 쓸 때 POST방식으로 구현하는 것이 좋다. 

