from flask import Blueprint,render_template



bp = Blueprint('userdatamanage',__name__,url_prefix='/userdatamanage')

@bp.route('/userdata')
def manage_userdata():
    return render_template('userdata_display.html')