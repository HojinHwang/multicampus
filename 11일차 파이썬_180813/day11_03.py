# primary key 
# 테이블에 한개만 존재 
# 테이블 생성시 컬럼명 옆에 입력 
# create table 테이블명 
#   (컬럼명1 데이타타입1 primary key,
#    컬럼명2 데이타타입2 ....)

import pymysql

# DB 연결
conn = pymysql.connect(host='localhost', 
    port=3306, user='root', 
    passwd='1234',
    db='python',
    charset='utf8')
print('연결완료')

# 커서 생성 
cursor = conn.cursor()

# 테이블 생성 
cursor.execute('''create table if not exists member 
(id int primary key, 
 membername text, gender text, age int);''')
# db 반영
conn.commit()

# 레코드 삽입 
# id 값이 같은 레코드 삽입시 예외처리 
try:
    cursor.execute(''' 
        insert into member (id, membername, gender, age)
        values (3,'이민영','여',22)
    ''')
    # db 반영
    conn.commit()
except:    
    pass

# 테이블조회 
cursor.execute('select * from member;')
result_list = cursor.fetchall()
print(result_list)


conn.close()
