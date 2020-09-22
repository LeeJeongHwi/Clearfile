# Flask_Login

### 1. Flask_Login

* 사용자를 체크하는 기능을 담당하는 라이브러리
  * 사용자 로그인시, Flask_login 라이브러리를 사용하면 사용자 관련 **session**정보를 HTTP response에 넣어줌
  * 이를 기반으로 flask 서버에서 사용자를 구별할 수 있는 기능을 제공

* Session
  * request를 1회성을 여러번 할때, 동일한 사용자가 일정 시간 동안 보내는 Request 들을 Session

#### 주요 동작 방식

* 사용자가 로그인 하면 로그인 정보를 User Class에서 객체로 가져오고, LoginManager()에 추가하여 세션 생성
  * Flask 서버가 리턴시에 해당 세션 정보를 웹페이지에 송부
* Current_user  객체에 해당 객체가 저장됨
  * 주요 Attribute
    * current_user.id : 사용자 id
    * current_user.is_authenticated : 사용자가 로그인 되어있는지를 나타내는 값 (T/F)
    * 이외의 attribute은 userClass를 정의하면서, 필요에 따라 추가
* 로그인 후 웹페이지로 Flask 서버 접근시, 전달받은 세션 정보를 기반으로 접근



### Flask Login

* 초기설정

  * `app.secret_key = os.urandom(24)` : 세션을 만들때 랜덤한 값으로 키 생성(보안성 강화)
    * 기존에 있는 세션 정보는 사용할 수 없음

* 산전 선언 필요 함수

  ```python
  @login_manager.user_loader # USER ID를 기반으로 사용자 객체를 리턴
  def load_user(user_id):
      return User.get(user_id)
  ```

  * 유저 클래스를 어떻게 만들지 모르기 때문에, 내가 맞는 user class에 맞게 구현해야함

  ```python
  @login_manager.unauthorized_handler
  def unauthorized():
      return make_reponse(jsonify(success=False),401)
  ```

  * 로그인이 안된 사용자인 경우에, 해당 데코레이터에 이루어진 함수를 적용
    * 메인페이지를 보여주거나, 로그인 해달라는 메시지 출력하거나....



##### USER CLASS

```python
class User(UserMixin):
    def __init__(self,user_id,user_email,blog_id): #생성자
        self.id=user_id
        self.user_email = user_email
        self.blog_id = blog_id
    def get_id(self): #객체 아이디
        return str(self.id) 
    
    @staticmethod # 클래스가 객체로 만들어지지 않아도 미리 선언되어있음 User.get(id)만 해도 호출ok
    def get(user_id):
        mysql_db = conn.mysqldb()
        db_cursor = mysql_db.cursor()
        sql ~~  #사용자 정보 가져오는 쿼리
        db_cursor.execute(sql)
        user=db_cursor.fetchone()
        if not user:
            db_cursor.close()
            return None
		print(user)
        user = User(인자)
        db_cursor.close()
        return user
    @staticmethod
    def find(user_email):
    
    @staticmethod
    def create(user_email,blog_id): #객체 생성, 찾아주는 함수.. --> 사용자 관련 기능
        
    # 사용자 전체에게 해당되는 함수이므로,  Static 으로 선언한 것

```



