# -*- coding: utf-8 -*-
# @time    : 2023/10/1 11:14
# @file    : views.py
# @software: PyCharm

"""
"""
import random

from flask import Blueprint
from .models import *


blue = Blueprint('multiple', __name__)


@blue.route('/')
def index():
    return 'home'

# ---------------------- 1: N ----------------------
# 多表: 一对多
@blue.route('/addgrade/')
def add_grade():
    """
    添加班级数据
    :return:
    """
    grades = []
    for i in range(10):
        grade = Grade()
        grade.grade_name = 'Con' + str(random.randint(10, 99))
        grades.append(grade)
    # 添加
    try:
        db.session.add_all(grades)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.flush()

    return 'OK'


@blue.route('/addstu/')
def add_stu():
    """
    添加学生数据
    :return:
    """
    students = []
    for i in range(10, 20):
        stu = Student()
        stu.name = f'xin-{i}'
        stu.age = i
        stu.gradeid = random.randint(1, 10)
        students.append(stu)
    try:
        db.session.add_all(students)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.flush()

    return 'OK'


@blue.route('/update/')
def update_data():
    """
    修改数据
    :return:
    """
    # 使用第一条数据进行示例
    stu = Student.query.first()
    stu.age = 333
    db.session.commit()

    return 'OK'


@blue.route('/delete/')
def delete_data():
    """
    删除数据
    :return:
    """
    # 使用第一条数据进行示例
    stu = Student.query.first()
    db.session.delete(stu)
    db.session.commit()

    return 'OK'


@blue.route('/delgrade/')
def delete_grade():
    """
    删除班级
    :return:
    """
    grade = Grade.query.first()
    db.session.delete(grade)
    db.session.commit()

    return 'OK'


@blue.route('/getstu/')
def get_stu():

    # 查询某学生所在班级 反向引用 grade
    stu = Student.query.get(2)  # 查找 id = 2 的学生
    print(stu.name, stu.age)
    print(stu.gradeid, stu.grade, stu.grade.grade_name, stu.grade.id)
    '''
    xin-11 11
    5 <Grade 5> Con70 5
    '''

    # 查找某班级下所有学生
    grade = Grade.query.get(3)  # 班级 id = 3
    print(grade.grade_name)
    print(grade.grade_student)  # 所有学生
    for stu in grade.grade_student:
        print(stu.name, stu.age)
    '''
    Con73
    [<Student 3>, <Student 5>]
    xin-12 12
    xin-14 14
    '''

    return 'OK'


# ---------------------- N: M ----------------------
@blue.route('/adduser/')
def add_user():

    users = []
    for i in range(10):
        user = User()
        user.username = 'XIN' + str(random.randint(10, 99))
        users.append(user)
    # 添加
    try:
        db.session.add_all(users)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.flush()

    return 'OK'


@blue.route('/addmovie/')
def add_movie():

    movies = []
    for i in range(10):
        movie = Movie()
        movie.moviename = 'MOVIE-' + str(random.randint(10, 99))
        movies.append(movie)
    # 添加
    try:
        db.session.add_all(movies)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.flush()

    return 'OK'


@blue.route('/addcollect/')
def add_collect():

    # 用户收藏电影
    user = User.query.get(1)  # 拿到用户 id=1
    movie = Movie.query.get(1)  # 拿到电影 id=1
    # user.movies: 拿到用户收藏的电影
    # user.movies.append(movie): 添加收藏电影数据
    user.movies.append(movie)
    db.session.commit()

    return 'OK'