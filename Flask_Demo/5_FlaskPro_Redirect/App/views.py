# -*- coding: utf-8 -*-
# @time    : 2023/9/15 10:14
# @author  : w-xin
# @file    : views.py
# @software: PyCharm

"""
路由 + 视图函数
"""
from flask import Blueprint, redirect, url_for

blue = Blueprint('demo', __name__)


@blue.route('/')
def index():
    return 'index'


@blue.route('/redireact/')
def make_redirect():

    # url_for('蓝图名称.视图函数名')
    ret = url_for('demo.index')
    # return redirect('http://baidu.com')
    # return redirect('/')
    return ret