# -*- coding: utf-8 -*-
# @time    : 2023/10/1 11:14
# @file    : exts.py
# @software: PyCharm

"""
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def init_exts(app):

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)