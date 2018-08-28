# f_14_for.py
# 관련 모듈 불러오기 
from flask import Flask, render_template, request

# 객체 생성
app = Flask(__name__)

# 라우팅 - 연결 페이지 
@app.route('/')
def home():
    # /templates/for_main.html
    return render_template('for_main.html')

# 퀴즈 : 
# 구구단 모두를 출력하세요 
# 라우팅 - 연결 페이지 
@app.route('/gugu')
def gugu():
    # /templates/for_main2.html
    return render_template('for_main2.html')


# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)  