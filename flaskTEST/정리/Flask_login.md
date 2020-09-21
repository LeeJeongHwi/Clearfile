# Flask_Login

### 1. Flask_Login

* 사용자를 체크하는 기능을 담당하는 라이브러리
  * 사용자 로그인시, Flask_login 라이브러리를 사용하면 사용자 관련 **session**정보를 HTTP response에 넣어줌
  * 이를 기반으로 flask 서버에서 사용자를 구별할 수 있는 기능을 제공

* Session
  * request를 1회성을 여러번 할때, 동일한 사용자가 일정 시간 동안 보내는 Request 들을 Session

#### 주요 동작 방식

* 