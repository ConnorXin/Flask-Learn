# -*- coding: utf-8 -*-
# @time    : 2023/9/17 11:25
# @author  : w-xin
# @file    : views.py
# @software: PyCharm

"""
"""
from flask import Blueprint, request, render_template
from sqlalchemy import desc, or_, not_

from .models import *


blue = Blueprint('single', __name__)

@blue.route('/')
def index():
    return 'index'


# 单表操作
# 数据的增删改查
# 增: 添加数据
@blue.route('/useradd/')
def user_add():

    # # 实例化模型
    # u = tableName()
    # # 添加一条数据
    # u.name = 'xin'
    # u.age = 27
    # # id 不用设置 自动增加
    # # 加入数据库
    # db.session.add(u)  # 将 u 对象添加到 session 中
    # db.session.commit()  # 提交

    # 添加多条数据
    users = []
    for i in range(10, 30):
        u = tableName()
        u.name = 'xin' + str(i)
        u.age = i
        users.append(u)

    try:
        db.session.add_all(users)
        db.session.commit()
    except Exception as e:
        # 若上方 sql 语句有报错 则全部返回 全部撤销
        db.session.rollback()  # 回滚
        # 刷新 清空缓存
        db.session.flush()

        return 'fail: ' + str(e)


    return 'success'



@blue.route('/userdel/')
def user_del():
    """
    删: 删除数据
    1 找到要删除的数据
    2 执行删除操作
    :return: 操作状态
    """
    u = tableName.query.first()  # 查询到第一条数据
    db.session.delete(u)
    db.session.commit()

    return 'success'


@blue.route('/userupdate/')
def user_update():
    """
    改: 修改数据
    1 找到要修改的数据
    2 执行修改操作
    :return: 操作状态
    """
    u = tableName.query.first()  # 查询到第一条数据
    u.age = 1000
    db.session.commit()

    return 'success'


@blue.route('/userall/')
def user_get_all():

    # all() 返回所有数据 以列表的形式
    users = tableName.query.all()
    print(users)  # 打印的是对象

    # 打印的是 sql 语句
    # SELECT user.id AS user_id, user.name AS user_name, user.age AS user_age
    # FROM user
    # 类型不是字符串  <class 'flask_sqlalchemy.query.Query'>
    print(tableName.query, type(tableName.query))

    return 'success'


@blue.route('/userfilter/')
def user_get_filter():
    """
    filter query
    :return:
    """
    '''# filter(): 按条件过滤 一个 filter() 后面还能够继续 .filter()
    # 类似 sql 中的 WHERE
    users = tableName.query.filter()
    # <class 'flask_sqlalchemy.query.Query'>
    # 类型虽然与 all 相同 但是是个查询集 使用 list() 强转能够获得数据
    print(users, type(users))
    print(list(users))'''


    '''
    filter(): 类似 sql 中的 WHERE
    filter_by(): 只能用于等值操作
    '''
    # filter
    users = tableName.query.filter(tableName.age == 20)
    print(users)  # 打印的是 sql 语句
    print(list(users))  # list() 强转一下得到数据

    users_overtake20 = tableName.query.filter(tableName.age > 20)
    print('overtake20: ', list(users_overtake20))

    # filter_by
    # 参数只写属性即可  不可写两个等号
    users_by = tableName.query.filter_by(age=20)
    print('filter_by: ', list(users_by))

    return 'success'


@blue.route('/userget/')
def user_get_get():

    # get(): 查询对应主键的数据对象
    user = tableName.query.get(6)
    # <class 'App.models.tableName'>
    print(user, type(user))
    # 这是一个单条数据
    # 可以具体取到某个值
    print(user.name, user.age)

    return 'success'


@blue.route('/userfirst/')
def user_get_first():

    # first(): 获取第一条数据
    # 注意没有 last() 方法
    user = tableName.query.first()
    print(user)

    # first_or_404(): 若不存在第一条数据则抛出 404 错误
    # "GET /userfirst/ HTTP/1.1" 404 -
    user_404 = tableName.query.filter_by(age=100).first_or_404()
    print(user_404)

    return 'success'


@blue.route('/usercount/')
def user_get_count():

    # count(): 返回查询数据的数据条数
    users = tableName.query.filter().count()
    print(users)  # 19

    return 'success'


@blue.route('/userlimit_offset/')
def user_get_limit_offset():

    # limit(): 查询前几条数据
    # offset(): 跳过前几条数据

    # 表示跳过前3条数据获取前4条数据
    users = tableName.query.offset(3).limit(4)
    print(list(users))

    return 'success'


@blue.route('/usersort/')
def user_get_sort():

    # order_by(): 排序
    users = tableName.query.order_by('age')  # 以 age 排序  默认升序
    users_desc = tableName.query.order_by(desc('age'))  # 降序
    print(list(users))
    print(list(users_desc))

    return 'success'


@blue.route('/userlogistic/')
def user_get_logistic():

    # and_
    users_and = tableName.query.filter(tableName.age > 20, tableName.age < 25)  # 默认是 and
    print('and: ', list(users_and))
    # or_
    users_or = tableName.query.filter(or_(tableName.age > 25, tableName.age < 20))
    print('or: ', list(users_or))
    # not_
    user_not = tableName.query.filter(not_(or_(tableName.age > 25, tableName.age < 20)))
    print('not: ', list(user_not))

    return 'success'


@blue.route('/userattribute/')
def user_get_attribute():
    """
    查询属性
    :return:
    """
    # contains 包含某字符
    users = tableName.query.filter(tableName.name.contains('3'))
    print(list(users))
    # in_(): 在某序列中
    users = tableName.query.filter(tableName.age.in_([10, 20, 30, 3]))
    print(list(users))
    # startswith(), endswith()
    users_start = tableName.query.filter(tableName.name.startswith('xin'))
    users_end = tableName.query.filter(tableName.name.endswith('3'))
    print(list(users_start))
    print(list(users_end))

    return 'success'


@blue.route('/usergt/')
def user_get_gt():

    # __gt__: 大于
    users = tableName.query.filter(tableName.age.__gt__(25))  # 表示 age 大于25
    print(list(users))

    return 'success'


'''
分页 翻页
1 手动翻页
    offset().limit()
    数据: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 28, 19, 20
    页码: page = 1
    每页显示数量: per_page = 5
    page = 1: 1, 2, 3, 4, 5        offset(0).limit(5)
    page = 2: 6, 7, 8, 9, 10       offset(5).limit(5)
    page = 3: 11, 12, 13, 14, 15   offset(10).limit(5)
    page = 4: 16, 17, 18, 19, 20   offset(15).limit(5)
    ...
    page = n:                      offset((page - 1) * per_page).limit(per_page)
2 paginate 对象进行翻页
'''
@blue.route('/paginate/')
def get_paginate():

    page = int(request.args.get('page', 1))  # html 参数页码
    per_page = request.args.get('per_page', 5)
    print(page, type(page))
    print(per_page, type(per_page))

    # paginate() 显示当前在第几页
    # 查询数据
    p = tableName.query.paginate(page=page, per_page=per_page, error_out=False)
    '''
    p 对象的属性
    ! items: 返回当前页的内容列表
    has_next: 是否还有下一页
    has_prev: 是否还有上一页
    next(error_out=False): 返回下一页的 Pagination 对象
    prev(error_out=False): 返回上一页的 Pagination 对象
    ! page: 当前页页码 (从1开始)
    ! pages: 总页数
    per_page: 每页显示的数量
    prev_num: 上一页页码数
    next_num: 下一页页码数
    ! total: 查询返回的记录总数
    '''
    # items: 返回当前页的内容列表
    print(p.items)
    # has_next: 是否还有下一页
    print(p.has_next)  # bool
    # has_prev: 是否还有上一页
    print(p.has_prev)
    # next(error_out=False): 返回下一页的 Pagination 对象
    print(p.next(error_out=False))
    # prev(error_out=False): 返回上一页的 Pagination 对象
    print(p.prev(error_out=False))
    # page: 当前页页码 (从1开始)
    print(p.page)
    # pages: 总页数
    print(p.pages)
    # per_page: 每页显示的数量
    print(p.per_page)
    # prev_num: 上一页页码数
    print(p.prev_num)
    # next_num: 下一页页码数
    print(p.next_num)
    # total: 查询返回的记录总数
    print(p.total)

    return render_template('paginate.html', p=p)




