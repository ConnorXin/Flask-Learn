# -*- coding: utf-8 -*-
# @time    : 2023/9/17 9:58
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

    # 配置 sqlite 数据库
    db_uri = 'sqlite:///sqlite_singleTable.db'
    # # 配置 mysql
    # password = ''
    # database = ''
    # db_uri = f'mysql+pymysql://root:{password}@localhost:3306/{database}'  # mysql
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 插件绑定
    init_exts(app=app)

    return app
