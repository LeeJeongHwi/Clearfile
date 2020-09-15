## 파이썬 문법

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

