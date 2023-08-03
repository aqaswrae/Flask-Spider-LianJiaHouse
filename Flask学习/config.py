#配置文件

SECRET_KEY = "asdfasdfjasdfjasd;lf"
'''
1.防止跨站请求伪造（CSRF）攻击
Flask 使用 SECRET_KEY 来生成 CSRF 令牌以防止 CSRF 攻击。CSRF 攻击是一种恶意攻击方式，攻击者会盗用用户的身份，发送虚假请求给网站，尤其是在存在安全漏洞的站点
很容易受到攻击。
2.对 session 数据进行加密
在 Flask 中，session 可以保存用户信息和状态。 SECRET_KEY 提供了一种安全的手段来对 session 数据进行加密，从而保护敏感数据的安全，防止其他人恶意窃取。
'''

#数据库配置
HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'flask-lianjia'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)'

