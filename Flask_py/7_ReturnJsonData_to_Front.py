# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/12 17:49
# @File    :  7_ReturnJsonData_to_Front.py
# @IDE     :  PyCharm

"""
返回数据到前端页面
"""
from flask import Flask, make_response, json, jsonify


app = Flask(__name__)

# 使用 jsonify 方式进行修改前端数据类型时
# 要解决编码问题使用以下方法
app.json.ensure_ascii = False  # 支持中文


@app.route('/index')
def index():

    data = {
        'name': '张三'
    }
    # # make_response 将想要的数据返回给前端; 此时在 html 中的数据还是文本数据 Content-Type: text/html; charset=utf-8
    # response = make_response(json.dumps(data, ensure_ascii=False))  # json.dumps 将 python 字典 --> json string; ensure_ascii=False 让中文能够显示
    # # 需要将返回前端的数据转换为 json 数据
    # response.mimetype = 'application/json'
    response = jsonify(data)   # flask 可直接 --> json
    # return response
    return response


if __name__ == '__main__':

    app.run()
