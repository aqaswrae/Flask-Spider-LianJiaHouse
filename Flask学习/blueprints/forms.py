
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, SelectMultipleField, RadioField, BooleanField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, Regexp


#注册表单
class RegisterForm(FlaskForm):
    username = StringField(label='用户名',validators=[DataRequired("账号不能为 空"),Length(4, 10, message='账号非法，请输入4~10位字符')])
    password = StringField(label='密码',validators=[Length(min=6, max=20, message="密码格式错误！")])#,Regexp('[0-9a-zA-Z!@#$%^&*]{6,16}')]
    check_password = StringField(label='确认密码',validators=[DataRequired("确认密码 不能为空"),EqualTo('password')])
    submit = SubmitField()
#登录表单
class LoginForm(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired("账号不能为 空"), Length(4, 10, message='账号非法，请输入4~10位字符')])
    password = StringField(label='密码', validators=[Length(min=6, max=20, message="密码格式错误！")])  # ,Regexp('[0-9a-zA-Z!@#$%^&*]{6,16}')]
    submit = SubmitField()
#新房添加数据时的表单
class NewhouseinfoForm(FlaskForm):
    housename = StringField(label='小区名称',validators=[DataRequired("小区名称不能为空")])
    developer = StringField(label='开发商')
    location = StringField(label='地址',validators=[DataRequired("地址不能为空")])
    room = StringField(label='几室几厅')
    ty = StringField(label='房产类型')
    tag = StringField(label='房产标签')
    area = StringField(label='建筑面积')
    avgprice = StringField(label='均价')
    totalprice = StringField(label='总价')
    submit = SubmitField()
#二手房添加数据时的表单
class OldhouseinfoForm(FlaskForm):
    housename = StringField(label='小区名称',validators=[DataRequired("小区名称不能为空")])
    # developer = StringField(label='开发商')
    year = StringField(label='建造年份')
    location = StringField(label='地址',validators=[DataRequired("地址不能为空")])
    room = StringField(label='几室几厅')
    tag = StringField(label='房产标签',)
    area = StringField(label='建筑面积')
    avgprice = StringField(label='均价')
    totalprice = StringField(label='总价')
    submit = SubmitField()

#搜索框功能
class SearchForm(FlaskForm):
    content = StringField()
    submit = SubmitField()