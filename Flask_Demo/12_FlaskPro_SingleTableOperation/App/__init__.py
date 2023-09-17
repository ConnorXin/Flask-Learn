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


    return app
