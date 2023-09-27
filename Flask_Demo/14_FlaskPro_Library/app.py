# -*- coding: utf-8 -*-
# @time    : 2023/9/27 9:42
# @author  : w-xin
# @file    : app.py
# @software: PyCharm

"""
"""
from App import create_app


app = create_app()

if __name__ == '__main__':

    app.run(debug=True, port=5501)

