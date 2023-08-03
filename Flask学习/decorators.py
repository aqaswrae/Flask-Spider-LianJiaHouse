#装饰器

from functools import wraps
from flask import g,redirect

#@wraps(func)是一个Python装饰器，用于将被装饰函数的元数据复制到装饰器函数中。它可以解决装饰器的一些问题，
# 例如，在使用help()函数查看文档时，装饰器的元数据不会被记载到被装饰函数的元数据中去
def login_required(func):
    #保留func的信息
    @wraps(func)
    def inner(*args,**kwargs):
        if g.user:
            return func(*args,**kwargs)
        else:
            return redirect('/user/login')

    return inner


# def admin_required(func):
#     #保留func的信息
#     @wraps(func)
#     def inner(*args,**kwargs):
#         if g.admin:
#             return func(*args,**kwargs)
#         else:
#             return redirect('/user/login')
#
#     return inner