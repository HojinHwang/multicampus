# sqlite db 접속하기 

# sqlite3 파이썬 라이브러리 로딩
# 내장 모듈 
import sqlite3

# SQLITE3 파이썬 모듈 버전 - 2.6.0
print(sqlite3.version)
# SQLITE3 설치 버전 - 3.21.0
print(sqlite3.sqlite_version)

# 연결변수(conn) = sqlite3.connect('db파일 경로')
conn = sqlite3.connect('test.db')

# 작업변수(cursor)=연결변수(conn).cursor()
cursor = conn.cursor() #커서 생성

# SQL 명령 실행하기 
# 특정 컬럼(Title)만 조회하기  
cursor.execute('select Title from albums;')

# 특정 개수만큼  
result_list = cursor.fetchmany(10)
# 리스트 전체 출력 및 자료형 확인
print(result_list , type(result_list))


# slqlite DB 파일 연결해제 
conn.close()