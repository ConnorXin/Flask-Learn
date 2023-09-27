# -*- coding: utf-8 -*-
# @time    : 2023/9/27 9:43
# @author  : w-xin
# @file    : views.py
# @software: PyCharm

"""
1 在书籍的 book_index.html 中有一个 "查看所有书籍" 的超链接按钮 点击进入书籍列表 book_list.html 页面
2 在书籍的 book_list.html 中显示所有书名 点击书名可以进入书籍详情 book_detail.html
3 在书籍 book_detail.html 中可以点击该书的作者和出版社 进入作者详情的 author_detail.html 和出版社详情的 publisher_detail.html 的页面
"""
from flask import Blueprint, render_template, request
from .models import *


blue = Blueprint('library', __name__)

@blue.route('/')
def book_index():
    return render_template('book_index.html')


@blue.route('/booklist/')
def book_list():
    return render_template('book_list.html')


@blue.route('/bookdetail/')
def book_detail():
    return render_template('book_detail.html')