# f_19_extends_quiz.py
# 퀴즈 - 5개의 메뉴를 가진 사이트 만들기 

# 관련 모듈 불러오기 
from flask import Flask, render_template

# 객체 생성
app = Flask(__name__)

# 라우팅 - 연결 페이지 
@app.route('/')
def home():
    return render_template('showcase.html')

# 라우팅 - 연결 페이지 
@app.route('/service')
def service():
    return render_template('service.html')

# 라우팅 - 연결 페이지 
@app.route('/designers')
def designers():
    return render_template('designers.html')

# 라우팅 - 연결 페이지 
@app.route('/packages')
def packages():
    return render_template('packages.html')

# 라우팅 - 연결 페이지 
@app.route('/contact')
def contact():
    return render_template('contact.html')

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)  