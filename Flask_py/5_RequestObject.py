# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/12 17:16
# @File    :  5_RequestObject.py
# @IDE     :  PyCharm

"""
request 对象
request 包含前端发送过来的所有请求数据
"""
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:  # POST
        # 获取表单数据
        name = request.form.get('name')
        password = request.form.get('password')
        print(name)
        print(password)
        return 'this is post'

重定向
if __name__ == '__main__':

    app.run()