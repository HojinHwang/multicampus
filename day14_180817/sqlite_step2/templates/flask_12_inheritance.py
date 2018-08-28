from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home2.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/site/')
def site():
    return render_template('site.html')

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)  
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')