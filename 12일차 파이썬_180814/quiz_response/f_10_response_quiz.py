# 관련 모듈 불러오기 
from flask import Flask, render_template, request

# 객체 생성
app = Flask(__name__)

# 라우팅 - 연결 페이지 
@app.route('/')
def home():
    return render_template('form_submit_quiz.html')

# 결과처리 라우팅 
#form action
# request.form[폼필드name값] : 폼필드에서 입력한 값이 저장되어 있다.


@app.route('/result', methods=['POST'] )
def action():
	username = request.form['username']
	useremail = request.form['useremail']
	userphone = request.form['userphone']
	message = request.form['message']
	# return '완료'
	return render_template('form_result_quiz.html', username=username, useremail=useremail, userphone=userphone, message=message)


if __name__ == '__main__':
    app.run(debug=True)  
