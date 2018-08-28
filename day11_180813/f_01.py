# 모듈 불러오기 
from flask import Flask

# app 객체 생성 
app = Flask(__name__)

# 라우터데코레이터 - url 관리 
# http://127.0.0.1:5000/ -> 무엇을 보여줄것인가?
@app.route('/')
# 뷰함수 -> 화면 표시 함수 
def hellow_world():
    #텍스트, html 태그 가능 
    return "<h1 style='text-align:center'> \
        hellow world</h1> \
        <p> \
          <a href='/test'>test 페이지로 이동</a> \
          <br><br> \
          <a href='/gallery'>gallery 페이지로 이동</a> \
        </p> " 

# 홈으로 이동하기, gallery 페이지로 이동하기 
# 하이퍼링크 소스 삽입
# http://127.0.0.1:5000/test
@app.route('/test/')    
def test():
    return "test page"

# 홈으로 이동하기, test 페이지로 이동하기 
# 하이퍼링크 소스 삽입
# http://127.0.0.1:5000/gallery
@app.route('/gallery/')    
def gallery():
    return "<h1 style='text-align:center'> \
    gallery page </h1> \
    <img src='/static/test.jpg'> "


# 앱 실행
if __name__ == '__main__':
    app.run()


