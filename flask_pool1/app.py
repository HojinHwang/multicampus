# app.py
# pip install DBUtils
from flask import Flask, render_template

from controllers.admin import admin
from controllers.api import api
from controllers.blog import blog

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# http://localhost:5000/admin
app.register_blueprint(admin, url_prefix='/admin')

# http://localhost:5000/api
app.register_blueprint(api, url_prefix='/api')

# http://localhost:5000/blog
app.register_blueprint(blog, url_prefix='/blog')

if __name__ == '__main__':
    app.debug = True
    app.run()
