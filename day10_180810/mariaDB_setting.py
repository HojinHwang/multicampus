# pip install pymysql
import pymysql

conn = pymysql.connect(host='127.0.0.1', 
    port=3306, user='root', 
    passwd='1234',
    db='classicmodels')

print('연결완료')
    
conn.close()

