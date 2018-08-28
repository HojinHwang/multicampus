# controllers/blog.py
from flask import Blueprint, render_template

blog = Blueprint('blog', __name__, template_folder='blog')

# http://localhost:5000/blog/
@blog.route("/")
def list():
    return render_template('blog/list.html')

@blog.route('/create')
def create():
    return 'create blog'

@blog.route('/read')
def read():
    return 'read blog'

@blog.route('/update')
def update():
    return 'update blog'

@blog.route('/delete')
def delete():
    return 'delete blog'
