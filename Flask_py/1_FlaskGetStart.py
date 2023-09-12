# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/12 14:34
# @File    :  1_FlaskGetStart.py
# @IDE     :  PyCharm

"""
official document: https://flask.palletsprojects.com/en/2.3.x/
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello World</p>"


if __name__ == '__main__':

    app.run()






