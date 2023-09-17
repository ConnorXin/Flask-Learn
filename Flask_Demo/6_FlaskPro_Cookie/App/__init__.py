# -*- coding: utf-8 -*-
# @time    : 2023/9/15 10:13
# @author  : w-xin
# @file    : __init__.py.py
# @software: PyCharm

"""
初始化文件 创建 Flask 应用
"""
from flask import Flask
from .views import *


def create_app():

    app = Flask(__name__)

    # 蓝图需要与 Flask 绑定
    # 注册蓝图
    app.register_blueprint(blueprint=blue)
    return app


