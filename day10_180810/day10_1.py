# sqlite db 접속하기 

# sqlite3 파이썬 라이브러리 로딩
# 내장 모듈 
import sqlite3

# SQLITE3 파이썬 모듈 버전 - 2.6.0
print(sqlite3.version)
# SQLITE3 설치 버전 - 3.21.0
print(sqlite3.sqlite_version)

# 샘플 DB - test.db
# 파이썬 작업 폴더에 저장한다. 

# 연결변수(conn) = sqlite3.connect('db파일 경로')
conn = sqlite3.connect('test.db')

# 작업변수(cursor)=연결변수(conn).cursor()
cursor = conn.cursor() #커서 생성

# SQL 명령 실행하기 
# 작업변수(cursor).excute('SQL 쿼리 명령')
# 모든 테이블의 데이터 조회하기 
# select * from 테이블명 limit 레코드수;
# cursor.execute('select * from albums limit 5;')
cursor.execute('select * from albums;')

# 작업변수(cursor).fetchall() -  파이썬 파일로 저장 
# 리스트 구조 - 각 요소는 튜플
# fetchall() - 테이블 데이타 모두 저장 
# fetchone() - 테이블 데이타 1개만 저장 
# fetchmany(숫자) - 숫자 수만큼 데이터 저장 
# 전체 
# result_list = cursor.fetchall()
# 1개만 
result_list = cursor.fetchone()
# 리스트 전체 출력 및 자료형 확인
print(result_list , type(result_list))

# 리스트요소 하나씩 출력하기 
for i in result_list:
    print(i)

print('전체 리스트 요소 수는? ', len(result_list))

# slqlite DB 파일 연결해제 
conn.close()