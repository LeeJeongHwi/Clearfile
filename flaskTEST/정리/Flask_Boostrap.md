### Flask 정적 웹페이지 로드

* ```render_template(HTML파일명)``` : HTML 파일 전송

#### BootStrap

* HTML Template 같은 것임
* 쓸려면 static url path를 변경시켜주어야함

#### Static URL Path

* `app = Flask(__name__, static_url_path='/static')`
  * 모든 Static 파일들은 여기에 넣겠다! 라는 뜻
  * 따라서 이 곳에 CSS , JS 등등 static 파일들을 여기에 넣는다
* `<form class="form-signin" action='/login' method='get'>`
  * action 에는 라우팅 경로를 작성
  * 해당 form에서 Button 클릭시 action으로 login 으로 라우팅된다
  * method는 default 로 get 방식으로 된다.