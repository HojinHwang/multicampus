# flask_16_sqlite.py
import sqlite3
from flask import Flask, render_template, request

# DB 연결 
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

def newTable():
    # 테이블 생성하기 
    cursor.execute(''' create table if not exists persons 
        (username text, userage int, usergender text, usermajor text );
    ''')
    # DB에 반영
    conn.commit()
    # 조회 
    cursor.execute('select * from persons;')
    result_list = cursor.fetchall()
    print(result_list)
# newTable()

# 테이블에 데이타에 삽입하기 
# sql = 'insert into persons values (?,?,?,?);'
# cursor.execute(sql, ('홍수미',22,'여','식품영양학과'))
# conn.commit()
# # 조회 
# cursor.execute('select * from persons;')
# result_list = cursor.fetchall()
# print(result_list)

# 데이터 입력함수 
def inserData(username,userage,usergender,usermajor):
    sql = 'insert into persons values (?,?,?,?);'
    cursor.execute(sql, (username,userage,usergender,usermajor))
    conn.commit()    

# 데이터 입력함수 실행 
# inserData('김준수',21,'남','기계공학과')

# 조회
def showTable_list():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select * from persons;')
    result_list = cursor.fetchall()
    return result_list

print(showTable_list())

# 플라스트 생성 
app = Flask(__name__)

# 라우팅 - 연결 페이지 
@app.route('/')
def home():
    return render_template('sqlite2_index.html')

# 라우팅 - 연결 페이지 
@app.route('/showtable')
def showtable():
    showTable_list()
    result_list = showTable_list()
    return render_template('showtable.html',result=result_list)


# 플라스트 실행 
if __name__ == '__main__':
    app.run(debug=True)  

# DB 닫기 
conn.close()

