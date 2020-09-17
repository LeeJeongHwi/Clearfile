

### MVP 버전

* 최소한의 기능을 구현한 제품
* 고객의 피드백을 받아서, 기능을 점차적으로 개선

# MVC 패턴

* Model - View - Controller 아키텍쳐
  * Model : 응용 프로그램의 데이터 (주로 DB)
  * View : 텍스트, 버튼 등 사용자 인터페이스 (웹페이지) - 일종의 Templates
  * Controller : Model과 View를 제어하는 중간 역할 (중간 제어 코드) - 
* 유지보수가 쉬워진다는 가정이 있음
  * 실제로는.. 여러파일로 쪼개져 있어서 코드 이해 및 디버깅이 어려움
  * 코드 수정시 특정 부분을 수정하기 보다는 전체 연결된 기능 관련 코드를 전부 수정해야 하는 경우가 더 많을 때도 있다.



### Blueprint

* 소스 코드를 분리시킬때 유용함

* 여러 소스 파일에 Flask 코드를 작성할 수 있또록 하는 기능

* ```python
  from flask import Flask,blueprint
  
  from 하위폴더 import 소스파일
  
  app = Flask(__name__)
  app.register_blueprint(소스파일.객체이름,url_prefix='/라우팅경로')
  ```

  * url_prefix : URL/url_prefix 경로/라우팅 경로 식으로 진행됨

* 분리된 하위 폴더의 소스파일

  * `Blueprint(블루프린트 이름,name)`

  * ```python
    from flask import Blueprint
    blog_abtest = Blueprint('blog',__name__)
    
    @blog_abtest.route("/blog1")
    def blog():
        return "blueprint test login--..."
    ```

