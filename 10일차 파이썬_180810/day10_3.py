
# sqlite3 파이썬 라이브러리 로딩
# 내장 모듈 
import sqlite3

# 연결변수(conn) = sqlite3.connect('db파일 경로')
conn = sqlite3.connect('naverDB.db')

# 작업변수(cursor)=연결변수(conn).cursor()
cursor = conn.cursor() #커서 생성

# SQL 명령 실행하기 
cursor.execute('select * from userTable;')

# 특정 개수만큼  
result_list = cursor.fetchall()
# 리스트 요소 각각 출력 
for i in result_list:
    print('레코드 - ', i)

# slqlite DB 파일 연결해제 
conn.close()