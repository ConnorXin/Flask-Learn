# -*- coding: utf-8 -*-
# @time    : 2023/9/17 11:25
# @author  : w-xin
# @file    : views.py
# @software: PyCharm

"""
"""
from flask import Blueprint
from .models import *


blue = Blueprint('single', __name__)

@blue.route('/')
def index():
    return 'index'

