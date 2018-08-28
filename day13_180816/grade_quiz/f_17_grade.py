# f_17_grade.py
# 입력필드에서 과목의 성적을 입력받은 후 
# 총점과 평균을 출력하여라 
# 그리고 평균이 70점을 넘으면 '진급 축하', 그렇지 않으면 
# '다음기회에' 출력

# 관련 모듈 불러오기 
from flask import Flask, render_template, request

# 객체 생성
app = Flask(__name__)

# 라우팅 - 연결 페이지 
@app.route('/')
def home():
    return render_template('form_grade.html')

# 결과페이지 
@app.route('/grade_result', methods=['POST'])
def result():
    kor = request.form['kor']
    eng = request.form['eng']
    tot = int(kor) + int(eng)
    return render_template('form_grade_result.html', \
        kor=kor, eng=eng, tot=tot )

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)  