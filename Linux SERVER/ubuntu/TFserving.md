# Tnesorflow Serving, Docker 에서 실행시키기

도커는 설치되어 있다고 가정한다.



1. 모델 학습

   * 학습 후 model을 `model.save(PATH)` 에 저장한다.

2. 경로 설정

   * 현재 진행 중인 프로젝트에서 save 한 모델의 주소는 다음과 같다.

     `/home/username/Dockers/servingModel/powerPredict/1` , 여기서 1은 버전을 의미함

3. TF serving 설치는 [공식사이트](https://www.tensorflow.org/install/docker?hl=ko) 를 참고했다.

4. 명령어를 사용해서 Tensorflow Serving을 실행시킨다.

`docker run -t --rm -p 8501:8501 --name tfserve -v "/home/userName/Dockers/servingModel/powerPredict:/models/power_model" -e MODEL_NAME=power_model tensorflow/serving`

* Container name을 tfserve 로 설정하고 tensorflow/serving images를 사용한다.
* -v 옵션을 사용해서 `"Loacl에 있는 모델PATH":"/models/[설정하고 싶은 모델네임]"` 으로 설정한다.
  * `/models/Modelname` 은 컨테이너 내에 있는 `models` 폴더안에 `modelname` 이름으로 만든 폴더와 local 모델 폴더와 연동시킨 것
* -e (환경설정),  REST API URL로 사용할 model_name을 지정한다.



5. 파이썬에서 request  보내기

```python
def predict(data_two_hour,n_input):
    headers= {"content-type":"application/json"}
    data = json.dumps({"sgnature_name":"serving_default","instances":data_two_hour})
    json_response = requests.post("http://localhost:8501/v1/models/power_model/versions/1:predict",data=data,headers=headers)
    predictions = json.loads(json_response.text)["predictions"]
    return predictions[0]
```

* 내가 현재 사용하고 있는 프로젝트에서 모델은 인풋-> 예측값을 보내주는 모델이다

```python
history = [float(x) for x in data_.values]
history.append(history[0]) ; history.append(history[1])
n_seq = 1
n_steps = 2
n_input = n_seq * n_steps
predictions = []
for i in range(2,len(history)):
    x_input = [history[i-2],history[i-1]]
    yhat = predict(x_input,n_input)
    predictions.append(yhat)
print(len(predictions)) # 8760
```

* 성공적으로 데이터를 보냈음을 확인할 수 있다.



##### 주의할 점

* Train 시킬 때 input을 꼭 기억하고 있어야한다.

  * 모델에 input을 주고 예측을 받아내는 구조다. 

    > TF serving은 그 역할을 REST API 형태로 수행한다.

* 포트 번호를 8501로 안하면 이상하게 되지 않았다. 이유는 왜인지 모르겠으나 공식사이트를 좀 더 찾아보면 나올 것 같다.