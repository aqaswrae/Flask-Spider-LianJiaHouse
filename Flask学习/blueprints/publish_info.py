from flask import Blueprint,render_template,redirect,request,url_for,g
from .forms import NewhouseinfoForm,OldhouseinfoForm
from exts import db
from models import NewHouseModel,OldHouseModel
from decorators import login_required



bp = Blueprint('pubinfo',__name__,url_prefix='/publishinfo')



@bp.route('/newhouseinfo',methods=['GET','POST'])
def publish_newhouseinfo():
    # if not g.admin:
    #     return redirect('user/adminlogin')
    form = NewhouseinfoForm(request.form)
    if request.method == 'GET':
        print('请求方式为GET')
        return render_template('newhousepubinfo.html', form=form)
    else:
        print('请求方式为POST')
        if form.validate():
            print('数据验证通过')
            housename = form.housename.data
            developer = form.developer.data
            location = form.location.data
            room = form.room.data
            ty = form.ty.data
            tag = form.tag.data
            area = form.area.data
            avgprice = form.avgprice.data
            totalprice = form.totalprice.data
            houseinfo = NewHouseModel(housename=housename,developer=developer,location=location,room=room,ty=ty,tag=tag,area=area,avgprice=avgprice,totalprice=totalprice)
            db.session.add(houseinfo)
            db.session.commit()
            return redirect('/displayinfo/newhouseinfo')
        else:
            print('数据验证未通过！')
            print(form.errors)
            return redirect('/publishinfo/newhouseinfo')

@bp.route('/oldhouseinfo',methods=['GET','POST'])
def publish_oldhouseinfo():
    form = OldhouseinfoForm(request.form)
    if request.method == 'GET':
        print('请求方式为GET')
        return render_template('oldhousepubinfo.html',form=form)
    else:
        print('请求方式为POST')
        if form.validate():
            print('数据验证通过')
            housename = form.housename.data
            # developer = form.developer.data
            year = form.year.data
            location = form.location.data
            room = form.room.data
            tag = form.tag.data
            area = form.area.data
            avgprice = form.avgprice.data
            totalprice = form.totalprice.data
            houseinfo = OldHouseModel(housename=housename,year=year,location=location,room=room,tag=tag,area=area,avgprice=avgprice,totalprice=totalprice)
            db.session.add(houseinfo)
            db.session.commit()
            return redirect('/displayinfo/oldhouseinfo')
        else:
            print('数据验证未通过！')
            print(form.errors)
            return redirect('/publishinfo/oldhouseinfo')
