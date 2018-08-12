
# sqlite3 파이썬 라이브러리 로딩
import sqlite3

# db가 없다면 새로 생성 
conn = sqlite3.connect('store.db')
cursor = conn.cursor() #커서 생성

# 테이블 생성 
cursor.execute(''' create table if not exists pTable(
                            pcode text,
                            pName text,
                            prce integer,
                            amount integer
 ); ''')

sql = 'insert into pTable values(?,?,?,?);'
items = [('p001','노트북', 110 , 5),
        ('p002','노트북',3,22),
        ('p003','노트북',1,11)]
cursor.executemany(sql,items)    

conn.commit() # DB 반영
# 데이터 조회 
cursor.execute('select * from pTable;')
pTable_list = cursor.fetchall();
print(pTable_list)

# end DB
conn.close()


