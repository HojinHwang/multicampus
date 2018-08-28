# flask_15_sqlite.py
import sqlite3
from flask import Flask, render_template, request

# 플라스트 생성 
app = Flask(__name__)


# 라우팅 - 연결 페이지 
@app.route('/')
def home():
    # 각 페이지로 이동하는 하이퍼링크 삽입
    return render_template('sqlite_table.html')


# 라우팅 - 연결 페이지 
@app.route('/employees')
def employees():
    # DB 연동 - 연결
    conn = sqlite3.connect('test.db')
    # 실행자 생성
    cursor = conn.cursor()
    # sql 명령 실행 
    # employees 테이블의 모든 데이터를 조회해라 
    cursor.execute(' select LastName, FirstName, Title from employees; ')
    # 리스트로 저장하기 
    result = cursor.fetchall()
    # print(result)
    # db 종료 
    conn.close()
    # 레코드 보내기 -> templates/sqlite_index.html 
    return render_template('sqlite_index.html', result=result)

# 라우팅 - 연결 페이지2 : 
@app.route('/list5')
def list5():
    # DB 연동 - 연결
    conn = sqlite3.connect('test.db')
    # 실행자 생성
    cursor = conn.cursor()
    # sql 명령 실행 
    # employees 테이블의 모든 데이터를 조회해라 
    cursor.execute(' select * from genres limit 7')
    # 리스트로 저장하기 
    result = cursor.fetchall()
    # print(result)
    # db 종료 
    conn.close()
    # 레코드 보내기 -> templates/sqlite_list5.html 
    return render_template('sqlite_list5.html', result=result)



# 플라스트 실행 
# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)  



