# -*- coding: utf-8 -*-
# @time    : 2023/9/12 23:13
# @author  : w-xin
# @file    : 9_CustomError.py
# @software: PyCharm

"""
自定义错误
"""
from flask import Flask, request, render_template, abort


app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'connor' and password == 'xin0420':
            return 'login success'
        else:
            abort(404)
            return None

# 自定义错误处理
@app.errorhandler(404)
def handle_404_error(err):
    return f'出现了404错误 错误信息:{err}'  # 也可以跳转页面


if __name__ == '__main__':

    app.run()
