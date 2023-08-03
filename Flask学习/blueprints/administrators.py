from flask import Blueprint


bp = Blueprint('admin',__name__,url_prefix='/admin')

@bp.route('/login')
def login():
    pass