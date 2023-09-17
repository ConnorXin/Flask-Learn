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

from flask import Blueprint, render_template, request, redirect, session

# 创建蓝图
blue = Blueprint('user', __name__)


# 路由可以是多个
@blue.route('/')
@blue.route('/home/')
def home():

    # 4 获取 session
    username = session.get('user')  # 'user' 要用下面那个 session 中的 user
    # 让 config 中的过期时间有效
    session.permanent = True

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
            # 3 设置 session
            session['user'] = username
            return response
        else:
            return '用户名或密码错误'


@blue.route('/logout/')
def logout():

    response = redirect('/home/')
    # 5 删除 session
    session.pop('user')
    # 清空 session 谨用!!! 会删除服务器上的所有 session
    # session.clear()

    return response
