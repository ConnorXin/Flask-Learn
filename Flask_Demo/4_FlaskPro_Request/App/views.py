# -*- coding: utf-8 -*-
# @time    : 2023/9/15 10:14
# @author  : w-xin
# @file    : views.py
# @software: PyCharm

"""
路由 + 视图函数
"""
# from . import create_app
from flask import Blueprint, request


# 引入一个概念 蓝图
# 创建蓝图
blue = Blueprint('request', __name__)


@blue.route('/request/', methods=['GET', 'POST'])
def get_request():

    # print(request)  # <Request 'http://127.0.0.1:5000/request/' [GET]>
    # 重要属性
    # 请求方法
    print(request.method)
    # GET 请求参数
    # http://192.168.51.18:5000/request/?name=list&name=wang&age=33
    # ImmutableMultiDict([('name', 'list'), ('name', 'wang'), ('age', 33)])
    print(request.args)
    print(request.args['name'])  # 若 Key 不存在报错
    print(request.args.get('name'))  # 若 Key 不存在不会报错 返回 None
    print(request.args.getlist('name'))  # 多个相同的 key 时使用
    # POST 请求参数
    # requests.post('http://192.168.51.18:5000/request/', data={'name': 'lucy', 'age': 33})
    print(request.form)
    print(request.form.get('name'))
    # cookie
    print(request.cookies)

    return 'request ok'


