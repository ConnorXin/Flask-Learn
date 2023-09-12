# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/12 18:39
# @File    :  8_abort_Func.py
# @IDE     :  PyCharm

"""
类似 python 的 raise: 主动抛出异常
abort: 在网页中抛出异常
"""
from flask import Flask, abort, request, render_template


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


if __name__ == '__main__':

    app.run()
