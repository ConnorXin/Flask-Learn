# -*- coding: utf-8 -*-
# @time    : 2023/9/16 21:48
# @author  : w-xin
# @file    : models.py
# @software: PyCharm

"""
放置模型
模型       -->      数据库
类        -->      表结构
类属性    -->      表字段
一个对象  -->      表的一行数据


数据迁移的详细步骤
1 安装数据迁移的包
2 在 exts.py 中初始化 Migrate, SQLAlchemy
3 在 models 中定义好模型
4 在 views.py 中导入 models 模块
5 配置好数据库 sqlite3 or MySQL
6 执行数据迁移命令
    6.1 cmd or Terminal 进入项目目录 (app.py 所在目录)
    6.2 输入命令
        flask db init      创建迁移文件夹 migrates, 只调用一次
        flask db migrate   生成迁移文件: 自动找到继承了 db.Model 的类
            迁移文件: Generating E:\github\Flask-Learn\Flask_Demo\10_FlaskPro_ModelBasic\migrations\versions\8051822c632a_.py
        flask db upgrade   执行迁移文件中的升级  生成表结构
        flask db downgrade 执行迁移文件中的降级  相当于撤销上一步的升级
7 查看数据库内容
    第一次使用需要下载数据库驱动 自己 download 下载
"""
from .exts import db


class User(db.Model):
    """
    必须继承 db.Model 才是模型
    """
    __tablename__ = 'tb_user'  # 表明
    # Integer: 整型
    # primary_key: 主键
    # autoincrement: 自动增长
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 字段
    # String: varchar(30), 可变字符串
    # unique: 约束, 不允许出现重复值
    # index: 设置普通索引
    name = db.Column(db.String(30), unique=True, index=True)
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.Boolean, default=True)
    # default: 设置默认值
    # nullable: 是否允许为空
    salary = db.Column(db.Float, default=100000, nullable=False)
    # 对表结构进行修改需要从 `flask db migrate` 开始重新迁移文件
    comm = db.Column(db.Float, default=100000, nullable=True)
