# -*- coding: utf-8 -*-
# @time    : 2023/9/17 11:23
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

    # mysql
    db_uri = 'mysql+pymysql://root:333333@localhost:3306/flask_db1'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化插件
    init_exts(app=app)

    return app
