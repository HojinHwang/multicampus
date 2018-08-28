# controllers/admin.py
from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, template_folder='admin')

# http://localhost:5000/admin/
@admin.route("/")
def list():
    # return 'admin list'
    return render_template('admin/list.html')

@admin.route('/create')
def create():
    return 'create admin'

@admin.route('/read')
def read():
    return 'read admin'

@admin.route('/update')
def update():
    return 'update admin'

@admin.route('/delete')
def delete():
    return 'delete admin'
