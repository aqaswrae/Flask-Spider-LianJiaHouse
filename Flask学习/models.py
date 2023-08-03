# 定义数据库模型。定义数据库表对应的模型类,可以通过 SQLAlchemy 提供的 db.Model 创建模型类
from exts import db


#管理员模型
class AdminModel(db.Model):
    __tablename__ = 'administrator'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    adminname = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(20),nullable=False)
# 用户模型
class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(20),nullable=False)
# 新房数据模型
class NewHouseModel(db.Model):
    __tablename__ = 'newhouseinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    housename = db.Column(db.String(20),nullable=False)
    #开发商
    developer = db.Column(db.String(20))
    location = db.Column(db.String(50))
    room = db.Column(db.String(20))
    ty = db.Column(db.String(15))
    tag = db.Column(db.String(40))
    area = db.Column(db.String(15))
    avgprice = db.Column(db.String(10))
    totalprice = db.Column(db.String(20))

    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship(UserModel,backref='houses')

# 二手房数据模型
class OldHouseModel(db.Model):
    __tablename__ = 'oldhouseinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    housename = db.Column(db.String(20),nullable=False)
    #开发商
    # developer = db.Column(db.String(20),nullable=False)
    year = db.Column(db.String(10))
    location = db.Column(db.String(50))
    room = db.Column(db.String(20))
    tag = db.Column(db.String(40))
    area = db.Column(db.String(15))
    avgprice = db.Column(db.String(10))
    totalprice = db.Column(db.String(20))

    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship(UserModel,backref='eshouses')