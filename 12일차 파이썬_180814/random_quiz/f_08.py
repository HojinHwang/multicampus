# 관련 모듈 불러오기 
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('f_08.html')

# http://127.0.0.1:5000/user/홍길동
@app.route('/user/<userid>')
def user(userid):  
    return '당신의 아이디는 %s' % (userid)

# http://127.0.0.1:5000/username/
#  -> 디폴트값 출력
# http://127.0.0.1:5000/username/홍길동
#  ->  홍길동
@app.route('/username/')
@app.route('/username/<username>')
def username(username='윤봉길'):  
    return render_template('f_08_name.html', \
    username=username)

# import random
# random.choice([값1, 값2, 값3...])
@app.route('/gift/<userid>')
def gift(userid):  
    choice = random.choice(['스타벅스 5만원권', \
    '현금100만원','문화상품권 40만원', \
    '수박 한통','꽝', '꽝'])
    return render_template('f_08_gift.html', \
        choice=choice,userid=userid)




if __name__ == '__main__':
    app.run(debug=True)  
