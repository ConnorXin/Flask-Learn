# -*- coding: utf-8 -*-
# @time    : 2023/9/15 10:14
# @author  : w-xin
# @file    : views.py
# @software: PyCharm

"""
路由 + 视图函数
"""
# from . import create_app
import datetime

from flask import Blueprint, render_template, request, redirect

# 创建蓝图
blue = Blueprint('user', __name__)


# 路由可以是多个
@blue.route('/')
@blue.route('/home/')
def home():

    # 4 获取 cookie
    username = request.cookies.get('user')  # 'user' 要用下面那个 set_cookie 中的 user

    return render_template('home.html', username=username)


@blue.route('/login/', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # 1 获取前端提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        # 2 模拟登录: 用户名和密码验证
        if username == 'list' and password == '333':
            response = redirect('/home/')
            # 3 设置 cookie
            # value 不能是中文
            # 默认浏览器关闭则 cookie 失效
            '''response.set_cookie('user', username)'''
            # max_age: s default
            '''response.set_cookie('user' ,username, max_age=3600*24*7)'''
            # expires: 也可设置过期时间
            response.set_cookie('user', username, expires=datetime.datetime(2023, 12, 12))
            return response
        else:
            return '用户名或密码错误'


@blue.route('/logout/')
def logout():

    response = redirect('/home/')
    # 5 删除 cookie
    response.delete_cookie('user')

    return response
