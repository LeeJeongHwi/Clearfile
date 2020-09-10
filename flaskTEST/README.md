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

### GET - POST 방식

