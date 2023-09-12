# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/12 17:24
# @File    :  6_Redirect.py
# @IDE     :  PyCharm

"""
重定向
302状态码就是重定向
1 访问网页时 点击按钮跳转到另外一个按钮
2 访问网页时 网页不需要了跳转到其他网页但是用户信息保留
"""
from flask import Flask, redirect, url_for


app = Flask(__name__)

# TODO redirect one
@app.route('/index')
def index():
    return redirect('https://www.baidu.com')  # url


# TODO redirect two
@app.route('/example')
def example():
    return redirect(url_for('redirect_two'))  # custom fun

# 要将 example 的路由匹配到 redirect 2 这里
@app.route('/redirect_2')
def redirect_two():
    return 'this is method two'


if __name__ == '__main__':

    app.run()
