# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/9/12 15:44
# @File    :  3_CustomConverter.py
# @IDE     :  PyCharm

"""
自定义转换器
需要模块进行设置
"""
from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)

# TODO Custom Convert
# 继承 BaseConverter
class RegexConverter(BaseConverter):
    """
    自定义转换类
    """
    def __init__(self, url_map, regex):

        super(RegexConverter, self).__init__(url_map)  # url_map 使用父类中的 init 初始化方法 就不需要再写一遍
        self.regex = regex

    def to_python(self, value):
        """
        父类方法
        :param value:
        :return:
        """
        print('to_python be called')
        return value

# 将自定义转换器添加到 flask 应用中
app.url_map.converters['re'] = RegexConverter


# TODO Begin
@app.route('/index/<re("1\d{10}"):value>')  # re 内传入 rule  正则: 首字符1开头后面10位
def index(value):
    print(value)
    return 'hello'


if __name__ == '__main__':

    app.run()