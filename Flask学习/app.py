import config,time,datetime,threading
from flask import Flask,render_template,session,g
from exts import db
from models import UserModel,AdminModel
from blueprints.user import bp as user_bp
from blueprints.administrators import bp as admin_bp
from blueprints.publish_info import bp as publish_bp
from blueprints.displaydata import bp as display_bp
from blueprints.userdata_management import bp as userdatamanage_bp
from blueprints.generate_chart import bp as datavisual_bp
from blueprints.delete_data import bp as delete_bp
from flask_migrate import Migrate
# from dataspider.newdataspider import new_timer
# from dataspider.olddataspider import old_timer
from werkzeug.utils import import_string
'''
from werkzeug.utils import import_string
使用延迟导入：Flask 提供了 from werkzeug.utils import import_string 函数，可以使用该函数进行延迟导入，可以避免模块之间的循环引用。
'''
'''
在Flask中，g是应用程序上下文对象，它是一个全局变量，可以在一个请求的生命周期内存储数据，可以在同一请求内的不同函数之间共享。它的作用类似于其他框架中的上下文。
通过在应用程序上下文对象中存储数据，可以在整个请求处理期间访问这些数据，而不需要在每个函数调用中传递它们。
例如，可以将数据库连接存储在g对象中，以便在请求处理期间的不同函数中共享它。g对象只在当前请求的线程上下文中可用，因此它是线程安全的。
'''



from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

#绑定配置文件
'''
用于加载配置的方式之一，它从指定的 config 对象中加载配置项并将其应用于 Flask 应用程序实例
在 config 模块中，通常会定义一个名为 Config 的类，它包含各种属性来表示配置项
使用 from_object() 方法将该配置类引入并进行加载
通过执行 app.config.from_object(Config)，Config 类中的所有属性都将被复制到 app.config 对象中，
这样应用程序就可以通过 app.config["DEBUG"]、app.config["SQLALCHEMY_DATABASE_URI"]、app.config["SECRET_KEY"] 等属性来访问它们。
这种方式使得配置的管理更加方便灵活，同时也提高了代码的可维护性和可读性。
'''
app.config.from_object(config)
#db与app绑定
db.init_app(app)#将 Flask 应用程序实例 app 与 db 对象关联起来，以便在 Flask 应用程序中使用数据库

migrate = Migrate(app,db)#将 Flask 应用程序实例 app 与数据库操作对象 db 关联起来，以便在应用程序中进行数据库迁移管理

#注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(publish_bp)
app.register_blueprint(display_bp)
app.register_blueprint(userdatamanage_bp)
app.register_blueprint(datavisual_bp)
app.register_blueprint(delete_bp)

# ORM模型映射成表的三步
# 1.flask db init 这步只需要执行一次
# 2.flask db migrate  识别ORM模型的改变，生成迁移脚本
# 3.flask db upgrade  运行迁移脚本，同步到数据库中

# 在app.config中设置好连接数据库的信息
# 然后使用SQLAlchemy(app)创建一个db对象
# SQLAlchemy会自动读取app.config中连接数据库的信息

#
# db = SQLAlchemy(app)
#
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone())

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

'''
@app.before_request 装饰的函数将会在请求之前执行，可以用于处理请求、验证用户身份、记录请求日志等。
在 Flask 中，如果我们需要在每个请求之前执行一些操作，可以使用 @app.before_request 装饰器来定义一个处理函数。
该函数将被注册到应用程序，每个请求都会在处理之前运行该函数。
我们定义了一个名为 my_before_request 的函数，并使用 @app.before_request 装饰它。该函数会在每次请求到达服务器之前先运行，并记录请求和请求的 URL。
'''
#两个钩子函数
@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    admin_id = session.get('admin_id')
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g,'user',user)#将 user 对象赋值给 g 对象的 user 属性
    else:
        setattr(g,'user',None)
    if admin_id:
        admin = AdminModel.query.get(admin_id)
        setattr(g,'admin',admin)
    else:
        setattr(g,'admin',None)

'''
在 Flask 中，@app.context_processor 装饰器是用于普通函数的特殊装饰器，它可以将一些变量添加到应用程序的上下文中，以便在所有模板上下文中使用。
具体来说，@app.context_processor 装饰器可以实现在应用中创建全局变量，方便在不同的模板中使用。
'''
#上下文处理器
@app.context_processor
def my_context_processor():
    return {'user':g.user}
@app.context_processor
def my_context_processor2():
    return {'admin':g.admin}



new_crawler = import_string('dataspider.newdataspider:crawler')
old_crawler = import_string('dataspider.olddataspider:crawler')
def func1():
    print(time.strftime('%Y-%m-%d %X'))
    print('爬虫程序要疯狂的运转了！！！')

def timer():
    while True:
        now = datetime.datetime.now()
        # print(now.hour,now.minute)
        if now.hour == 3 and now.minute == 10:
            func1()
            new_crawler()
            old_crawler()
            break
# t1 = threading.Thread(target=timer)
# t1.setDaemon(True)#设置守护进程
# t1.start()


if __name__ == '__main__':
    app.run()


