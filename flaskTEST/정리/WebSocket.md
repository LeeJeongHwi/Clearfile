# WebSocket

#### 정의

* 한 컴퓨터가 다른 컴퓨터와 상호 작용할 수 있는 경로를 설정
* "게이트"가 열려있을 때, 즉 소켓이 열려 있는 경우에만 통신을 가능케함 
* 실시간 데이터 처리에 있어서 Socket은 필수

> **HTTP 방식은 데이터가 업데이트 될 때 아예 "새로운 페이지"를 생성하는 느낌이다.**
>
> --> HTTP는 연결디 외서 html 문서 등 정리가 다 되었다면 연결이 **끊기는** 특징을 가지고 있기 때문
>
> 따라서 WebSocket 같은 경우 통로를 열어두는 것이니기 때문에, 통로에 데이터를 집어넣는 느낌이다.

--> 실시간 채팅에 주로 사용됨!

### SocketIO

* JavaScript를 이용하여 브라우저 종류에 상관없이 실시간 웹을 구현할 수 있도록 한 기술

### Flask-SocketIO

* 구버전 익스플로러에서는 작동하지 않는다.
* Flask에서도 SocketIO를 사용할 수 있게 구현해 놓은 라이브러리

#### Test ) 실시간 채팅 

##### Back

* ```python
  #Reference : https://github.com/josharnoldjosh/simple-flask-socketio-example
  from flask import *
  from flask_socketio import *
  
  # Init the server
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'some super secret key!'
  socketio = SocketIO(app, logger=True)
  
  # Send HTML!
  @app.route('/')
  def root():    
      return "Hello world!"
  
  # Returns a random number
  @app.route('/random')
  def random():  
      from random import randint  
      html = str(randint(1, 100))
      return html
  
  # Prints the user id
  @app.route('/user/<id>')
  def user_id(id):
      return str(id)
  
  # Display the HTML Page & pass in a username parameter
  @app.route('/html/<username>')
  def html(username):
      return render_template('chat.html', username=username)
  
  # Receive a message from the front end HTML
  @socketio.on('send_message')   
  def message_recieved(data): # Front에서 넘긴 data(Json)
      print(data['text'])
      emit('message_from_server', {'text':'Message recieved!'},broadcast=True) # 연결되어있는 모두에게 전송
  
  # Actually Start the App
  if __name__ == '__main__':
      """ Run the app. """    
      socketio.run(app, port=8000, debug=True)
  ```

  * `@socketio.on(event,namespace)`
    * 해당 "event"가 들어오면 함수 내부에 있는 emit(event, json,broadcast=False) 으로 사용자(sender)에게 전송
    * broadcast=True 시, 모든 사용자에게 전송
    * namespace는 어떤 socket에 대해 데이터를 주고 받을 것인가?를 결정

##### Front (All Code)

* ```html
  <html>
      <head>
          <!-- Some basic meta info -->
          <title>Example</title>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
  
          <!-- A stylesheet to make things automatically look nice -->
          <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.min.css">
  
          <!-- Link to the socket.io info -->
          <script type="text/javascript" src="//code.jquery.com/jquery-1.4.2.min.js"></script>
          <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"></script>
  
          <!-- Script to handle socket.io -->
          <script>
              var socket;            
              $(document).ready(function() {
                  // The http vs. https is important. Use http for localhost!
                  socket = io.connect('http://' + document.domain + ':' + location.port);
  
                  // Button was clicked
                  document.getElementById("send_button").onclick = function() {
                      // Get the text value
                      var text = document.getElementById("textfield_input").value;
  
                      // Update the chat window
                      document.getElementById("chat").innerHTML += "You: " + text + "\n\n";                    
                      
                      // Emit a message to the 'send_message' socket	
                      socket.emit('send_message', {'text':text});
  
                      // Set the textfield input to empty
                      document.getElementById("textfield_input").value = "";
                  }
  
                  // Message recieved from server
                  socket.on('message_from_server', function(data) {
                      var text = data['text'];
                      document.getElementById("chat").innerHTML += "Server: " + text + "\n\n";   
                  });
              });
          </script>
      </head>
  
  <body>
      <div style="margin: 25px; display: flex; flex-direction: column;">
          <h1 class="title">Hello {{username}}.</h1>
          <p>Welcome to the flask quick start example.</p>                        
          <textarea id="chat" style="width: 500px; height: 250px; font-size: 18px; font-family: monospace; margin-top: 10px;"></textarea>                 
          <div style="display: flex; flex-direction: row;">
              <input type="text" id="textfield_input" style="height: 30px; width: 400px; margin-top: 5px; margin-right: 10px;" class="textfield"> 
              <button id="send_button" class="button is-primary" style="margin-top: 5px; width: 90px; height: 30px;">Send</button>
          </div>
      </div>        
  </body>
  </html>
  ```

* 전체 코드는 다음과 같다.

**Detail of SocketCode**

* ```html
  <!-- Script to handle socket.io -->
  <script>
      var socket;            
      $(document).ready(function() {
          // The http vs. https is important. Use http for localhost!
          socket = io.connect('http://' + document.domain + ':' + location.port); // Socket 연결
  
          // Button was clicked
          document.getElementById("send_button").onclick = function() { //Send 버튼 클릭
              // Get the text value
              var text = document.getElementById("textfield_input").value; // ID를 통해서 해당 Textfield의 value를 가져옴
  
              // Update the chat window
              document.getElementById("chat").innerHTML += "You: " + text + "\n\n";  //innerHTML로 HTML내에 표시한다.
  
              // Emit a message to the 'send_message' socket
              socket.emit('send_message', {'text':text}); // "SEND_MESSAGE" 라는 Event를 호출하고 인자로 Json을 넘긴다.
  
              // Set the textfield input to empty
              document.getElementById("textfield_input").value = ""; // 입력창 초기화
          }
  
          // Message recieved from server
          socket.on('message_from_server', function(data) { // "Message_from_server" Event로 넘어온 데이터를 처리(callback)
              var text = data['text'];
              document.getElementById("chat").innerHTML += "Server: " + text + "\n\n";   
          });
      });
  </script>
  ```
  * `socket.on`은 Server에서 보낸 emit을 받음
  * `socket.emit`은 Server에 있는 `socket.on("event")`로 event를 보냄
    * server에 요청하려면 emit
    * server로 부터 받는것은 on
  * `$(document).ready(function(){})`
    * "문서가 준비되면 실행되는 함수"
    * 문서(document) 객체가 모두 로드 된 다음에 실행될 코드들을 해당 callback 함수 내에 기술해줘야함
    * DOM(Document Object Model)

> SocketIO는 비동기식처리방식이다

#### 결과물

![image-20201027170751136](./SocketIOTEST)