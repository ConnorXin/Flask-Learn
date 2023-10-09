# -*- coding: utf-8 -*-
# @time    : 2023/10/1 11:14
# @file    : app.py
# @software: PyCharm

"""
"""
from App import create_app


app = create_app()


if __name__ == '__main__':

    app.run(debug=True)