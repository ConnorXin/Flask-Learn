# -*- coding: utf-8 -*-
# @time    : 2023/9/16 21:53
# @author  : w-xin
# @file    : exts.py
# @software: PyCharm

"""
放置 flask 插件的 py 文件
三个步骤
"""
# 1 导包
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# 2 初始化
db = SQLAlchemy()  # ORM
migrate = Migrate()

# 3 与 app 对象绑定
def init_exts(app):

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
