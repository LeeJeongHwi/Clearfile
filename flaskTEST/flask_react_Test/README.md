# Flask (+React + MySQL)

<img src="https://img.shields.io/badge/Python-3.8.5-green"><img src="https://img.shields.io/badge/Flask-1.1.2-green"> <img src="https://img.shields.io/badge/MySQL-8.0.15-red"><img src="https://img.shields.io/github/last-commit/LeeJeongHwi/Study-repo">

### Install

해당프로젝트는 Flask와 MySQL을 이용했습니다. **"requirements.txt"** 를 확인하시고 패키지 설치 후 TEST를 진행하시길 바랍니다.

```python
> pip install -r requirements.txt
```

### Usage

```python
python run.py
```

만약 map_info 에 해당하는 테이블이 존재하지 않다면 map_info table을 만들어주세요.

INSERT는 해당 컬럼에 맞게 넣으시면 됩니다.



### React

https://github.com/201810824Hyunsomi/react_hook-map 와 연동되어 있습니다.

현재 `Axios` 연동이 안되어있으므로 테스트는 불가합니다.



##### MySQL Table Structure

* map_info Table

| Field     | Type             | Null | Key     | Extra          |
| --------- | ---------------- | ---- | ------- | -------------- |
| id        | int(10) unsigned | No   | Primary | Auto_increment |
| name      | varchar(255)     | YES  |         |                |
| latitude  | varchar(255)     | YES  |         |                |
| longitude | varchar(255)     | YES  |         |                |

### File Structure

```markdown
📦flask_react_Test
 ┣ 📂controller
 ┃ ┗ 📜controller.py
 ┣ 📂model
 ┃ ┣ 📜mapinfo.py
 ┃ ┗ 📜models.py
 ┣ 📂templates
 ┃ ┣ 📜chat.html
 ┃ ┗ 📜test.html
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┣ 📜run.py
```

* `models.py` 에서 Connection 정보를 수정하시길 바랍니다.
* `controller.py`는 Routing 처리를 하는 코드입니다.
* `run.py`는 Flask 서버를 구동시킵니다.



### Routing  (Controller.py)

* `/load_map` : 현재는 POST방식으로만 처리

  > id를 parameter로 전달받고 id에 해당하는 데이터를 json으로 Return한다.



