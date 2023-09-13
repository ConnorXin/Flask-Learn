# -*- coding: utf-8 -*-
# @time    : 2023/9/13 10:01
# @author  : w-xin
# @file    : 12_FlaskDB.py
# @software: PyCharm

"""
flask 数据库
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

class Config:
    """
    配置参数
    """
    pass


if __name__ == '__main__':

    app.run()