from flask import Blueprint,render_template,redirect
from decorators import login_required



bp = Blueprint('datavisualization',__name__,url_prefix='/datavisualization')

@bp.route('/avgprice')
def charts1():
    return render_template('二手房(小区名称-均价图).html')

@bp.route('/totalprice')
def charts2():
    return render_template('二手房(小区名称-总价图).html')

@bp.route('/distribution')
def charts3():
    return render_template('二手房(各地区-房产数量图).html')

@bp.route('/year')
def charts4():
    return render_template('二手房(年份--建造小区数量图).html')