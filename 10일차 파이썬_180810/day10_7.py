
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

# 데이터 수정하기 1
# sql 명령
# update 테이블명 set 컬럼명=새값 where 컬럼명 기존값;
# update books set recommended=100 where Title='스프링';
cursor.execute(''' update books 
          set recommended=100 
          where Title='스프링'; ''')
conn.commit() # DB 반영          

printTable()

# 데이터 수정하기 2
# ?를 이용한 방식 
# sql변수= 
#   'update 테이블명 set 컬럼명=? where 컬럼명=?;'
# cursor.execute(sql변수,('',''))
sql = 'update books set pages=? where Title=?;'
cursor.execute(sql,(300,'파이썬'))


printTable()

# end DB
conn.close()


