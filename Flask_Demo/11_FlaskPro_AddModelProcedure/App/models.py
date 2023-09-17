# -*- coding: utf-8 -*-
# @time    : 2023/9/17 10:02
# @author  : w-xin
# @file    : models.py
# @software: PyCharm

"""
"""
from .exts import db


class User(db.Model):
    """
    必须继承 db.Model 才是模型
    """
    __tablename__ = 'tb_user'  # 表明
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 字段
    name = db.Column(db.String(30), unique=True, index=True)
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.Boolean, default=True)
    salary = db.Column(db.Float, default=100000, nullable=False)
    comm = db.Column(db.Float, default=100000, nullable=True)
