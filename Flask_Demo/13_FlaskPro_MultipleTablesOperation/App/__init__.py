# -*- coding: utf-8 -*-
# @time    : 2023/10/1 11:14
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

    db_uri = 'mysql+pymysql://root:333333@localhost:3306/multiple_db'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_exts(app=app)

    return app

