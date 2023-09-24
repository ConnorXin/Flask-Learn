# -*- coding: utf-8 -*-
# @time    : 2023/9/17 11:25
# @author  : w-xin
# @file    : models.py
# @software: PyCharm

"""
"""
from .exts import db


class tableName(db.Model):

    __tablename__ = 'user'
    # columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer, default=1)

    def __repr__(self):
        """
        将对象 tableName 的打印转换成 self.name 的内容
        :return:
        """
        return self.name

