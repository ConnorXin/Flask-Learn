# -*- coding: utf-8 -*-
# @time    : 2023/9/15 10:14
# @author  : w-xin
# @file    : views.py
# @software: PyCharm

"""
路由 + 视图函数
"""
# from . import create_app
from flask import Blueprint

# 不能这样写 因为 App 只能有一个 Flask 应用
# 在 app.py 中已经调用过一次了
# app = create_app()


# 引入一个概念 蓝图
# 创建蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    return 'index'


@blue.route('/product/')
def product():
    return 'product'
