# f_16_for_dict.py
# 관련 모듈 불러오기 
from flask import Flask, render_template, request

myDict = { 'name':'이장화', 'age':20,  \
'school':'서초고등학교' }
print(myDict)
print(myDict['name']) # 이장화
# 키값만 출력하기 
for key in myDict:
    print(key)
# 키와 값 출력하기 
'''
name 이장화
age 20
school 서초고등학교
'''
for key,value in myDict.items():
    print(key,value)

# 객체 생성
app = Flask(__name__)

# 라우팅 - 연결 페이지 
@app.route('/')
def home():
    dic = {'user':'hong1001','addr':'서울 도봉구', 
    'phone':'010-4563-9090'}
    # /templates/for_dict_main.html
    return render_template('for_dict_main.html',dic=dic)

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)  