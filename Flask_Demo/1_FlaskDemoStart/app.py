# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/14 19:08
# @File    :  app.py
# @IDE     :  PyCharm

"""
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':

    app.run()