# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/14 19:28
# @File    :  app.py
# @IDE     :  PyCharm

"""
模板渲染
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask Home'


@app.route('/index')
def index():
    return render_template('index.html', name='法外狂徒张三')


if __name__ == '__main__':

    # debug: 开启调试模式 代码修改后会自动重启
    # port: default 5000
    # host: 默认 127.0.0.1; 指定 0.0.0.0 代表本机所有 ip 从其他设备也能够访问
    # app.run(debug=True, port=5000, host='0.0.0.0')
    app.run(debug=True)