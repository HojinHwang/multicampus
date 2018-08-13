# 퀴즈 - 
# 부트스트랩 페이지 연결하기  
# https://startbootstrap.com 다운로드 


# 모듈 불러오기 
from flask import Flask, render_template

# app 객체 생성 
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/')
# 뷰함수 -> 화면 표시 함수 
# templates 폴더 아래의 index.html 로 연결 
# index.html 에 삽입된 이미지는 static 폴더로 이동 
# img 주소 변경하기 - /static/~
def home():
    return render_template('index3.html')


# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)


