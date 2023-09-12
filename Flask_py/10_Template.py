# -*- coding: utf-8 -*-
# @time    : 2023/9/12 23:22
# @author  : w-xin
# @file    : 10_Template.py
# @software: PyCharm

"""
模板的应用
1 保持原有的 index2.html 不动将数据返回到前端
"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/index')
def index():
    data = {
        'name': '张三',
        'age': 18,
        'mylist': [1, 2, 3, 4, 5, 6]
    }
    return render_template('index2.html', data=data)


def list_step(li):
    """
    自定义过滤器
    :param li:
    :return:
    """
    return li[: : 2]


# 要让 list_step 过滤器给系统使用就要注册过滤器
# first param: custom name; second param: use name
app.add_template_filter(list_step, 'li2')



if __name__ == '__main__':

    app.run()