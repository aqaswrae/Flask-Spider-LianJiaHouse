#exts.py 这个文件是为了解决循环引用的问题
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()