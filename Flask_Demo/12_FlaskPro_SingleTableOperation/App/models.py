# -*- coding: utf-8 -*-
# @time    : 2023/9/17 11:25
# @author  : w-xin
# @file    : models.py
# @software: PyCharm

"""
"""
from exts import db


class tableName(db.Model):

    __tablename__ = 'name'
    # columns
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)


