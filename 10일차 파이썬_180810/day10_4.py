
# sqlite3 파이썬 라이브러리 로딩
import sqlite3

# 연결변수(conn) = sqlite3.connect('db파일 경로')
# db가 없다면 새로 생성 
conn = sqlite3.connect('book.db')

cursor = conn.cursor() #커서 생성

# 테이블의 제목, 출판일자, 출판사, 페이지수, 추천여부 
# 테이블이 존재하지 않으면 생성 
# 테이블 생성 SQL
# create table if not exists 테이블명(컬럼명 데이터타입,...)
# books 테이블이 데이타베이스에 없다면 생성해라 
cursor.execute(''' create table if not exists books(
                            title text,
                            published_date text,
                            publisher text,
                            pages integer,
                            recommended integer
 ); ''')
# 결과 확인은 sqlite Expert 프로그램에서 book.db 불러와서 확인  

# 데이터 입력 - 첫번째 방식 
# SQL : insert into 테이블명 values('','','',,);
cursor.execute(''' insert into books 
             values('자바','2009-09-01','영진',300,400
             ) ; ''')
cursor.execute(''' insert into books 
             values('스프링','2009-10-01','에이콘',600,50
             ) ; ''')             

conn.commit() # DB 반영
# 데이터 조회 
cursor.execute(' select * from books;')
book_list = cursor.fetchall();
print(book_list)

# end DB
conn.close()