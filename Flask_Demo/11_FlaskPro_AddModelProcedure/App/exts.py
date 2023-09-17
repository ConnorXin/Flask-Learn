# -*- coding: utf-8 -*-
# @time    : 2023/9/17 10:02
# @author  : w-xin
# @file    : exts.py
# @software: PyCharm

"""
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def init_exts(app):

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)