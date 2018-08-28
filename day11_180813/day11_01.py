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

# 접속된 db에 있는 테이블 조회 - usertable
cursor.execute('select * from usertable')

# 리스트로 저장하기 
result_list = cursor.fetchall()
# 전체 리스트 요소 찍기 
print(result_list)

for i in result_list:
    print(i)

# 2번째 레코드 찍기 
print(result_list[1])


conn.close()
