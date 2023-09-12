# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/12 14:50
# @File    :  2_FlaskRoute.py
# @IDE     :  PyCharm

"""
路由是生成 url  匹配函数和 url 关系
url 和函数的映射关系是 url 指向函数
"""
from flask import Flask


app = Flask(__name__)

# TODO route basic
@app.route('/hello', methods=['GET', 'POST'], endpoint='hello')
# 本身匹配的是 / 根目录; 需要在 url 后面加上 '/hello'
# method 表示访问 url 需要什么方式
def hello():
    return 'hello world'


# second 同理
@app.route('/hi', methods=['POST'])  # Method Not Allowed\nThe method is not allowed for the requested URL.
def hi():
    return 'hi!'


# 路由相同时 只匹配第一个
@app.route('/hello', methods=['GET', 'POST'])
def hello2():
    return 'hello hello world'


# 函数名相同 报错 error
@app.route('/hi', methods=['GET', 'POST'], endpoint='hello!')
def hello():
    return 'hi!'
'''
AssertionError: View function mapping is overwriting an existing endpoint function: hello
route 中设置不同 endpoint 就不会 error
但是 hello! 网页404
'''

# TODO route named rule
# @app.route('/user/<id>')
# def index(id):
#     """
#     判断 id 是否是我想要的地址
#     :param id:
#     :return:
#     """
#     if id == str(1):
#         return 'python'
#     elif id == str(2):
#         return 'django'
#     elif id == str(3):
#         return 'flask'
#     return 'hello world'

# 直接从前端中传入整型 不需要转换字符串: <int:*>
# 其中 int 可以替换 string, string 不接收斜杠文本
# float: 接收正浮点数
# path: 接收包含斜杠的文本
@app.route('/user/<int:id>')
def index(id):
    """
    判断 id 是否是我想要的地址
    :param id:
    :return:
    """
    if id == 1:
        return 'python'
    elif id == 2:
        return 'django'
    elif id == 3:
        return 'flask'
    return 'hello world'


if __name__ == '__main__':

    app.run()
