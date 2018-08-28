
# sqlite3 파이썬 라이브러리 로딩
import sqlite3

# db가 없다면 새로 생성 
conn = sqlite3.connect('book.db')
cursor = conn.cursor() #커서 생성

# 데이터 입력 - 세번째 방식 
# ?를 이용한 방식 
# sql변수= 'insert into 테이블명 values(?,?,?,?,?);'
# 리스트이름 = [('','','',,)...]
# cursor.executemany(sql변수,items)
sql = 'insert into books values(?,?,?,?,?);'
items = [('파이썬','2010-09-09','에이콘',500,300),
        ('유니티','2017-10-11','제이팝',800,300),
        ('포토샵','2015-09-30','에이콘',50,300)]
cursor.executemany(sql,items)    

conn.commit() # DB 반영
# 데이터 조회 
cursor.execute(' select * from books;')
book_list = cursor.fetchall();
print(book_list)

# end DB
conn.close()


