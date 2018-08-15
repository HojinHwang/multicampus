# 관련 모듈 불러오기 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
# 파이썬파일에서 값전달과 관련된 변수 선언 
    a = 'Python Start'
    b = 'Flask'
    c = 0
    for i in range(1,101):
        c += i
    print(c)
    return render_template('f_07.html', \
        a=a,b=b,c=c)


@app.route('/cal/')
def cal():
    a = 5
    b = 6
    result = a+b
    return render_template('f_07_cal.html', \
        result=result)

# f_07_cal.html 결과파일에 
# a = {{ a }}
# b = {{ b }}
# a+b = {{c }} ...

if __name__ == '__main__':
    app.run(debug=True)  
