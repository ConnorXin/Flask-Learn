# -*- coding: utf-8 -*-
# @time    : 2023/9/15 10:13
# @author  : w-xin
# @file    : __init__.py.py
# @software: PyCharm

"""
初始化文件 创建 Flask 应用
"""
from flask import Flask
from .views import *


def create_app():

    app = Flask(__name__)

    app.register_blueprint(blueprint=blue)

    # session config
    print(app.config)  # flask config
    '''
    <Config {'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None,
    'SECRET_KEY': None,
    'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31),
    'USE_X_SENDFILE': False, 'SERVER_NAME': None,
    'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session',
    'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None,
    'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False,
    'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True,
    'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': None,
    'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False,
    'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http',
    'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>
    '''
    app.config['SECRET_KEY'] = '333xin'
    # 要重新设置过期时间同理: 'PERMANENT_SESSION_LIFETIME'
    return app


