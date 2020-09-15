## Flask Jinja2



### Jinja2 템플릿

* **웹페이지 필요한 부분을 변경할 필요가 있을 때 사용하는 간단한 문법**

* 웹페이지에서 파이썬 프로그래밍

  ```python
  {{ 변수명 }}
  {% Python sourceCode %}
  ```

### Jinja2 템플릿 엔진

* Jinja2 템플릿엔진이 해당 HTML코드를 템플릿으로 만듬
* 템플릿 안에 파이썬 코드 실행
* 템플릿 채운 후 최종 **HTML 파일** 생성



#### base

* `<h1>Hello {{name}}</h1>`
  * 실제 HTML (템플릿 채운 후 최종 HTML 파일 생성하므로)
    `<h1>Hello JeongHwi</h1>`

#### 반복문

* `{% for %} {% endfor %}`

  * for 선언, endfor 로 마무리

* 들여쓰기는 안해도됨

  ```python
  {% for value in values %}
  {{value}}
  {% endfor %}
  ```

* range() : 파이썬과 동일

* len() : values | length

* loop.index : 반복문 횟수

  * 0,1,2,3.. 이아닌 1,2,3,4...로 시작

* values[] : 인덱싱

#### 조건문

* {% if %} {% elif %} {% else %} {% endif %} - 반복문과 동일



