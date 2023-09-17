# -*- coding: utf-8 -*-
# @time    : 2023/9/16 21:46
# @author  : w-xin
# @file    : views.py
# @software: PyCharm

"""
"""
from flask import Blueprint
from .models import *


blue = Blueprint('model', __name__)


@blue.route('/')
def index():
    return 'index / home'
