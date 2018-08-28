
# sqlite3 파이썬 라이브러리 로딩
import sqlite3

# db가 없다면 새로 생성 
conn = sqlite3.connect('book.db')
cursor = conn.cursor() #커서 생성

# 데이터 입력 - 두번째 방식 
# ?를 이용한 방식 
# sql변수= 'insert into 테이블명 values(?,?,?,?,?);'
# cursor.execute(sql변수,('','','', ,))
sql = 'insert into books values(?,?,?,?,?);'
cursor.execute(sql,('파이썬','2010-09-09','에이콘',500,300))   
cursor.execute(sql,('마리아DB','2011-12-12','길벗',500,300))   

conn.commit() # DB 반영
# 데이터 조회 
cursor.execute(' select * from books;')
book_list = cursor.fetchall();
print(book_list)

# end DB
conn.close()