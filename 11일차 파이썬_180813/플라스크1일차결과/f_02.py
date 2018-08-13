# 모듈 불러오기 
from flask import Flask

# app 객체 생성 
app = Flask(__name__)

# 라우터데코레이터 - url 관리 
# http://127.0.0.1:5000/ -> 무엇을 보여줄것인가?
@app.route('/')
# 뷰함수 -> 화면 표시 함수 
def hellow_world():
    return "Home"

# 동적 파라미터 전달하기 
# 함수로 인자 전달 
# http://127.0.0.1:5000/user/<값>
#  -> 뷰함수(인자) -> return 인자 
@app.route('/user/<userId>')
def users(userId):
    return 'user is %s' % userId

# 다수개의 파라미터 전달 
# http://127.0.0.1:5000/user2/tester/홍길동
@app.route('/user2/<userId>/<userName>')
def user2(userId, userName):
    return 'user ID - %s, user name - %s ' % (userId, userName)
# 값 제한 
# 기본 데이타 형이 string
# <데이타입:변수명>
# 데이타입 - <int:데이타변수명>, <float:데이타변수명>
@app.route('/news/<int:newsid>/<int:start>')
def news(newsid, start):
    # return "뉴스 %d %d" % (newsid, start)
    return "뉴스 %s %s" % (newsid, start)

'''
bbs/12/안녕
웹브라우저에 아래처럼 출력하도록 한다. 

글번호 : 12
내용 : 안녕

'''

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)


