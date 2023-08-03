from flask import Blueprint, render_template,request
from models import NewHouseModel, OldHouseModel,UserModel
from .forms import SearchForm
from decorators import login_required

bp = Blueprint('displayinfo', __name__, url_prefix='/displayinfo')


@bp.route('/newhouseinfo')
@login_required
def dispaly_newhouseinfo():
    newhouse_info = NewHouseModel.query.all()
    # 面积正序
    area_asc = NewHouseModel.query.order_by((NewHouseModel.area + 0)).all()
    # 面积倒序
    area_desc = NewHouseModel.query.order_by((NewHouseModel.area + 0).desc()).all()
    # 均价正序
    avg_asc = NewHouseModel.query.order_by((NewHouseModel.avgprice + 0)).all()
    # 均价倒序
    avg_desc = NewHouseModel.query.order_by((NewHouseModel.avgprice + 0).desc()).all()
    # 总价正序
    total_asc = NewHouseModel.query.order_by((NewHouseModel.totalprice+0)).all()
    # 总价倒序
    total_desc = NewHouseModel.query.order_by((NewHouseModel.totalprice+0).desc()).all()
    return render_template('user_nh_displaydata.html', newhouse_info=newhouse_info, area_asc=area_asc,area_desc=area_desc,avg_asc=avg_asc, avg_desc=avg_desc,total_asc=total_asc,total_desc=total_desc)

@bp.route('/adminnewhouseinfo')
def dispaly_adminnewhouseinfo():
    newhouse_info = NewHouseModel.query.all()
    # 面积正序
    area_asc = NewHouseModel.query.order_by((NewHouseModel.area + 0)).all()
    # 面积倒序
    area_desc = NewHouseModel.query.order_by((NewHouseModel.area + 0).desc()).all()
    # 均价正序
    avg_asc = NewHouseModel.query.order_by((NewHouseModel.avgprice + 0)).all()
    # 均价倒序
    avg_desc = NewHouseModel.query.order_by((NewHouseModel.avgprice + 0).desc()).all()
    # 总价正序
    total_asc = NewHouseModel.query.order_by((NewHouseModel.totalprice+0)).all()
    # 总价倒序
    total_desc = NewHouseModel.query.order_by((NewHouseModel.totalprice+0).desc()).all()
    return render_template('admin_newhouse_display.html', newhouse_info=newhouse_info, area_asc=area_asc,area_desc=area_desc,avg_asc=avg_asc, avg_desc=avg_desc,total_asc=total_asc,total_desc=total_desc)

@bp.route('/oldhouseinfo')
def display_oldhouseinfo():
    oldhouse_info = OldHouseModel.query.all()
    #建造年份正序
    year_asc = OldHouseModel.query.order_by((OldHouseModel.year+0)).all()
    #建造年份倒序
    year_desc = OldHouseModel.query.order_by((OldHouseModel.year+0).desc()).all()
    # 面积正序
    area_asc = OldHouseModel.query.order_by((OldHouseModel.area + 0)).all()
    # 面积倒序
    area_desc = OldHouseModel.query.order_by((OldHouseModel.area + 0).desc()).all()
    # 均价正序
    avg_asc = OldHouseModel.query.order_by((OldHouseModel.avgprice + 0)).all()
    # 均价倒序
    avg_desc = OldHouseModel.query.order_by((OldHouseModel.avgprice + 0).desc()).all()
    # 总价正序
    total_asc = OldHouseModel.query.order_by((OldHouseModel.totalprice+0)).all()
    # 总价倒序
    total_desc = OldHouseModel.query.order_by((OldHouseModel.totalprice+0).desc()).all()
    return render_template('user_oh_displaydata.html', oldhouse_info=oldhouse_info,year_asc=year_asc,year_desc=year_desc,area_asc=area_asc,area_desc=area_desc,avg_asc=avg_asc,avg_desc=avg_desc,total_asc=total_asc,total_desc=total_desc)

@bp.route('/adminoldhouseinfo')
def display_adminoldhouseinfo():
    oldhouse_info = OldHouseModel.query.all()
    #建造年份正序
    year_asc = OldHouseModel.query.order_by((OldHouseModel.year+0)).all()
    #建造年份倒序
    year_desc = OldHouseModel.query.order_by((OldHouseModel.year+0).desc()).all()
    # 面积正序
    area_asc = OldHouseModel.query.order_by((OldHouseModel.area + 0)).all()
    # 面积倒序
    area_desc = OldHouseModel.query.order_by((OldHouseModel.area + 0).desc()).all()
    # 均价正序
    avg_asc = OldHouseModel.query.order_by((OldHouseModel.avgprice + 0)).all()
    # 均价倒序
    avg_desc = OldHouseModel.query.order_by((OldHouseModel.avgprice + 0).desc()).all()
    # 总价正序
    total_asc = OldHouseModel.query.order_by((OldHouseModel.totalprice+0)).all()
    # 总价倒序
    total_desc = OldHouseModel.query.order_by((OldHouseModel.totalprice+0).desc()).all()
    return render_template('admin_oldhouse_display.html', oldhouse_info=oldhouse_info,year_asc=year_asc,year_desc=year_desc,area_asc=area_asc,area_desc=area_desc,avg_asc=avg_asc,avg_desc=avg_desc,total_asc=total_asc,total_desc=total_desc)

@bp.route('/userdata')
def display_userdata():
    userdata = UserModel.query.all()
    return render_template('userdata_display.html',userdata=userdata)

# 搜索框视图函数
'''
有新房数据和二手房数据,当使用搜索框功能的时候,无法设置筛选的哪个房型的数据,就是一个search函数接收两个房型数据的话,如何判断要搜索哪个房型的数据呢?
'''
@bp.route('/newsearch')
def search_new():
    q = request.args.get('q')
    print(q)
    newhouseinfo = NewHouseModel.query.filter(NewHouseModel.housename.contains(q)).all()
    print(newhouseinfo)
    return render_template('user_nh_displaydata.html',newhouseinfo=newhouseinfo)

@bp.route('/oldsearch')
def search_old():
    q = request.args.get('q')
    oldhouseinfo = OldHouseModel.query.filter(OldHouseModel.housename.contains(q)).all()
    return render_template('user_oh_displaydata.html',oldhouseinfo=oldhouseinfo)
