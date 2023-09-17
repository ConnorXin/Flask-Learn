# -*- coding: utf-8 -*-
# @time    : 2023/9/16 21:44
# @author  : w-xin
# @file    : __init__.py.py
# @software: PyCharm

"""
"""
from flask import Flask
from .views import *
from .exts import init_exts


def create_app():

    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)

    # 配置数据库
    db_uri = 'sqlite:///sqlite3.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    # 插件绑定
    init_exts(app=app)

    return app
