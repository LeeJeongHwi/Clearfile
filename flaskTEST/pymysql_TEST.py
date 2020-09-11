import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='rjdnf88as',
                     db='test',
                     charset='utf8')

def create_Query():
    sql = """
          CREATE TABLE test_table(
                idx INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(256) NOT NULL,
                nick VARCHAR(256) NOT NULL);
          """
    cursor.execute(sql) #쿼리문 실행
    db.commit()
def insert_Query():
    sql = """
          INSERT INTO test_table(name,nick) VALUES("test_name","test_nickName")
          """
    cursor.execute(sql)  # 쿼리문 실행
    db.commit()  # CREATE,DROP,DELETE,UPDATE,INSERT와 같이 database 내부의 데이터에 영향을 주는 함수의 경우 사용
def select_Query():
    sql = """SELECT * FROM test_table"""
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)
def update_Query():
    sql = """UPDATE test_table SET name ='%s',nick='%s' WHERE name='%s'""" %("new_test","new_nick","test_name")
    cursor.execute(sql)
    db.commit()

if __name__ == "__main__":
    try:
        with db.cursor() as cursor:
            select_Query()
            update_Query()
            select_Query()
    except:
        print("ERROR")

    db.close()