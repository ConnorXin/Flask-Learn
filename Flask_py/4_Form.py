# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/12 16:16
# @File    :  4_Form.py
# @IDE     :  PyCharm

"""
前端的表单如何与后端程序产生交互
如何关联 index.html
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():
    # 渲染模板 index.html
    return render_template('index.html')


if __name__ == '__main__':

    app.run()