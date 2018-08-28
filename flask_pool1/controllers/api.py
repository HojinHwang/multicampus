# controllers/api.py
from flask import Blueprint, render_template

api = Blueprint('api', __name__, template_folder='api')

# http://localhost:5000/api/
@api.route("/")
def list():
    return render_template('api/list.html')

@api.route('/create')
def create():
    return 'create api'

@api.route('/read')
def read():
    return 'read api'

@api.route('/update')
def update():
    return 'update api'

@api.route('/delete')
def delete():
    return 'delete api'
