# 组织 Flask 应用的代码：将相关的功能模块集中在一起，便于维护。
# 定义应用的 URL：蓝图可以定义自己的 URL，然后将视图函数与 URL 绑定起来。



from flask import Blueprint,render_template,redirect,url_for,request,session
# from flask_sqlalchemy import SQLAlchemy
from .forms import RegisterForm,LoginForm
from models import UserModel,AdminModel
from exts import db



bp = Blueprint('user',__name__,url_prefix='/user')


@bp.route('/login', methods=['GET','POST'])
def login():#用户登录
    form = LoginForm(request.form)
    if request.method == 'GET':
        print('请求方式为GET')
        return render_template('userlogin.html',form=form)
    else:
        print('请求方式为POST')
        if form.validate():
            print('数据验证通过')
            username = form.username.data
            password = form.password.data
            user = UserModel.query.filter_by(username=username).first()
            if not user:
                print('用户名在数据库中不存在')
                return redirect('/user/login')
            elif user.password == password:
                session['user_id'] = user.id
                if username == 'admin':
                    return redirect('/displayinfo/adminnewhouseinfo')
                else:
                    return redirect('/displayinfo/newhouseinfo')
            else:
                print('密码输入错误！')
                return redirect('/user/login')
        else:
            print('数据验证不通过')
            print(form.errors)
            return render_template('userlogin.html',form=form)

@bp.route('/adminlogin', methods=['GET','POST'])
def adminlogin():#管理员登录
    form = LoginForm(request.form)
    if request.method == 'GET':
        print('gly请求方式为GET')
        return render_template('admin_login.html',form=form)
    else:
        print('gly请求方式为POST')
        if form.validate():
            print('gly数据验证通过')
            username = form.username.data
            password = form.password.data
            user = AdminModel.query.filter_by(adminname=username).first()
            if not user:
                print('管理员在数据库中不存在')
                return redirect('/user/adminlogin')
            elif user.password == password:
                # print('[][][][]')
                session['admin_id'] = user.id
                return redirect('/displayinfo/adminnewhouseinfo')
            else:
                print('gly密码输入错误！')
                return redirect('/user/adminlogin')
        else:
            print('gly数据验证不通过')
            print(form.errors)
            return render_template('admin_login.html',form=form)


@bp.route('/register', methods=['GET','POST'])
def register():#注册
    form = RegisterForm(request.form)
    if request.method == "GET":
        print('请求方法为GET')
        return render_template('register.html', form=form)
    else:#request.method == "POST"
        print('请求方法为POST')
        if form.validate():  # 如果验证通过 # 获取数据
            username = form.username.data
            password = form.password.data
            check_password = form.check_password.data
            print(username, password, check_password)
            judgement = UserModel.query.filter_by(username=username).first()
            if judgement:
                print('该用户已存在')
                return redirect('/user/register')
            else:
                user = UserModel(username=username,password=password)
                db.session.add(user)
                db.session.commit()
                return redirect('/user/login')
        else:
            print('数据验证不通过')
            print(form.errors)
            return render_template('register.html', form=form)

#退出登录
@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
