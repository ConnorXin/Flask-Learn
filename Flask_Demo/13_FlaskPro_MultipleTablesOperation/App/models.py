# -*- coding: utf-8 -*-
# @time    : 2023/10/1 11:14
# @file    : models.py
# @software: PyCharm

"""
"""
from .exts import db


# ---------------------- 1: N ----------------------
class Grade(db.Model):
    """
    班级表
    """
    __tablename__ = 'grade'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    grade_name = db.Column(db.String(30))
    # 与学生表建立关联
    # 'Student': 关联的表类名
    # 'backref': 反向引用名称 得到一个对象 让 student 反过来得到 grade 对象名称
    #            可以这样使用: student.grade
    # lazy: 懒加载 只有使用关联时才加载关联
    grade_student = db.relationship('Student', backref='grade', lazy=True)


class Student(db.Model):
    """
    学生表
    """
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    # 班级外键
    gradeid = db.Column(db.Integer, db.ForeignKey(Grade.id))


# ---------------------- N: M ----------------------
# 用户表 电影表 关联用户表和电影表的中间表
# 中间表: 收藏表
collect = db.Table(
    'collects',
    db.Column('userid', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('movieid', db.Integer, db.ForeignKey('movie.id'), primary_key=True)

)

class User(db.Model):
    """
    电影用户表
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30))


class Movie(db.Model):
    """
    电影表
    """
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    moviename = db.Column(db.String(30))

    # 关联
    # secondary=collect: 关联上中间表
    # lazy='dynamic': 返回一个 query 对象 (查询集) 可以继续使用其他查询方法 如 all()
    # lazy='seelct': 首次访问到属性的时候 就会全部加载该属性的数据
    # lazy='joined': 在对关联的两个表进行 join 操作 从而获取到所有相关的对象
    # lazy=True: 返回一个可用的列表对象 同 select
    users = db.relationship('User', backref='movies', lazy='dynamic', secondary=collect)

