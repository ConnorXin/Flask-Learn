# -*- coding: utf-8 -*-
# @time    : 2023/9/27 9:42
# @author  : w-xin
# @file    : models.py
# @software: PyCharm

"""
"""
from .exts import db


class Author(db.Model):
    """
    作者表
    """
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.Boolean, default=True)
    email = db.Column(db.String(100))

    # 关系
    books = db.relationship('Book', backref='author', lazy='dynamic')


class Book(db.Model):

    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), unique=True)
    date = db.Column(db.DateTime)

    # 1: n  加入外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))



# 中间表  书籍 - 出版社
book_publisher = db.Table('book_publisher',
                          db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
                          db.Column('publisher.id', db.Integer, primary_key=True))


class Publisher(db.Model):
    """
    出版社表
    """
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    website = db.Column(db.String(100))

    # n: n  关联 book 表
    books = db.relationship('Book', backref='publishers', secondary=book_publisher, lazy='dynamic')