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

    data = {
        'name': 'xin',
        'age': 27,
        'likes': ['popping', 'dance', 'vocal']
    }

    return render_template('home.html', **data)


@blue.route('/templatesPlus/')
def templates_plus():

    data = {
        'name': 'xin',
        'age': 27,
        'likes': ['popping', 'dance', 'vocal']
    }

    return render_template('child_2.html', **data)


