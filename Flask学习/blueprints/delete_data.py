from flask import Blueprint, render_template, redirect, request, url_for, jsonify
from models import NewHouseModel,OldHouseModel,UserModel
from exts import db




bp = Blueprint('deletedata',__name__,url_prefix='/delete')


@bp.route('/deletenew',methods=['POST'])
def delete_new():
    data = request.json
    inputValue = data['inputValue']
    newhousedata = NewHouseModel.query.filter_by(id=inputValue).first()
    db.session.delete(newhousedata)
    db.session.commit()
    return redirect('/displayinfo/newhouseinfo')


@bp.route('/deleteold',methods=['POST'])
def delete_old():
    data = request.json
    inputValue = data['inputValue']
    oldhousedata = OldHouseModel.query.filter_by(id=inputValue).first()
    db.session.delete(oldhousedata)
    db.session.commit()
    return redirect('/displayinfo/oldhouseinfo')

@bp.route('/delete_row',methods=['POST'])
def delete_row():
    data = request.json
    inputValue = data['inputValue']
    userdata = UserModel.query.filter_by(id=inputValue).first()
    db.session.delete(userdata)
    db.session.commit()
    return redirect('/displayinfo/userdata')