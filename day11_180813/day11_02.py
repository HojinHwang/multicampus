# 터미널창에서 설치 
# pip install pymysql
# pip list
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
cursor.execute('''create table if not exists bbs 
(id int, contents text, writer text);''')
# db 반영
conn.commit()

# 레코드 삽입 
cursor.execute('''insert into bbs (id, contents, writer) 
    values(3,'수요일은 오지 마세요 푹 쉬세요','관리자2')
''')
# db 반영
conn.commit()
# 테이블조회 
cursor.execute('select * from bbs;')
result_list = cursor.fetchall()
print(result_list)

# 레코드 삭제 
cursor.execute('''
    delete from bbs where id=1;
''')
# db 반영
conn.commit()

# 레코드 업데이트 
cursor.execute(''' update bbs 
   set contents='오늘은 월요일 수요일 광복절은 쉽니다.'
   where id=2 
''')
# db 반영
conn.commit()

# 테이블조회 
cursor.execute('select * from bbs;')
result_list = cursor.fetchall()
print('-'*10)
print(result_list)


conn.close()
