
# sqlite3 파이썬 라이브러리 로딩
import sqlite3

# db가 없다면 새로 생성 
conn = sqlite3.connect('store.db')
cursor = conn.cursor() #커서 생성

# 테이블 생성 함수 정의 
def createTable():
    cursor.execute(''' create table if not exists pTable(
                                pcode text,
                                pName text,
                                prce integer,
                                amount integer
    ); ''')
    conn.commit() # DB 반영

# 테이블 생성 함수 호출 
createTable()

# 데이터 입력 함수 정의 
def insertData(items):
    sql = 'insert into pTable values(?,?,?,?);'
    cursor.executemany(sql,items)    
    conn.commit() # DB 반영

items = [('p004','노트북1', 110 , 5),
            ('p005','노트북2',3,22),
            ('p006','노트북3',1,11)]

# 데이터 입력 함수 호출
insertData(items)    

# 데이터 조회 함수 정의 
def printTable():
    cursor.execute('select * from pTable;')
    pTable_list = cursor.fetchall();
    print(pTable_list)

# 데이터 조회 함수 호출 
printTable()

# end DB
conn.close()


