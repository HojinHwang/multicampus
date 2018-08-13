# 특정 html 페이지 연결하기 
# 연결되는 html 페이지는 templates 폴더에
# 저장되어 있어야한다.
# //flask 작업시 주의 사항 
# -폴더 구조 유의 
# /static/ - 이미지, 동영상
# /templates/  - html 

# 모듈 불러오기 
from flask import Flask, render_template

# app 객체 생성 
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/')
# 뷰함수 -> 화면 표시 함수 
# templates 폴더 아래의 index.html 로 연결 
def home():
    return render_template('index2.html')

# http://127.0.0.1:5000/user
@app.route('/user')
# templates 폴더 아래의 user.html 로 연결 
def user():
    return render_template('user.html')


# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)


