# -*- coding: utf-8 -*-
# @time    : 2023/9/17 10:02
# @author  : w-xin
# @file    : views.py
# @software: PyCharm

"""
route and views
"""
from flask import Blueprint
from .models import *


blue = Blueprint('single_table', __name__)

@blue.route('/')
def index():
    return 'index'
