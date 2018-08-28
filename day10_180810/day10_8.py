
# sqlite3 파이썬 라이브러리 로딩
import sqlite3

# db가 없다면 새로 생성 
conn = sqlite3.connect('book.db')
cursor = conn.cursor() #커서 생성

# 데이터 조회 함수 정의 
def printTable():
    cursor.execute('select * from books;')
    books_list = cursor.fetchall();
    print('*'*20)
    print(books_list)

printTable()

# 데이터 삭제하기 1
# sql 명령
# delete from 테이블명 where 컬럼명=값;
# delete from books where publisher='영진';
cursor.execute("delete from books where publisher='영진';")
conn.commit() # DB 반영          

printTable()

# 데이터 삭제하기 2
# ?를 이용한 방식 
# sql변수= 
#   'delete from 테이블명 where 컬럼명=?;'
# 삭제할 값은 리스트정의후 값으로 삽입
# cursor.execute(sql변수,[리스트값])
# sql = 'delete from books where publisher=?;'
# cursor.execute(sql,['에이콘'])
sql = 'delete from books where publisher=?;'
cursor.execute(sql,['에이콘'])
conn.commit() # DB 반영 

printTable()

# end DB
conn.close()



