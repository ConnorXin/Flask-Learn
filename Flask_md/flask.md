# flask
是个轻量级后端框架

#flask 路由

#request 对象

#模板

#flask 数据库


#表单

#ajax

#管理系统 case

# 创建虚拟环境

在每一个项目开启 flask 开发前 创建单独的虚拟环境

```bash
cmd bash

windows:
pip install virtualenv virtualenvwrapper-win

查看虚拟环境
workon

创建新的虚拟环境: mkvirtualenv
mkvirtualenv flask2env

删除虚拟环境: rmvirtualenv

进入(切换)虚拟环境
worko flask2env
```

# Cookie

作用: 让服务器能够认识浏览器；常用于登录

![1694839255183](image/flask/1694839255183.png)


# 模型 Model

Flask 默认没有提供任何数据库操作的 API

可以选择任何适合自己项目的数据库来使用

Flask 中可以用原生 SQL 语句实现功能，也可以选择 ORM

## ORM

Flask 通过 Model 操作数据库，不管数据库是 MySQL 或者 Sqlite，Flask 自动帮你生成相应数据库类型的 SQL 语句，所以不需要关注 SQL 语句和类型，对数据的操作 Flask 帮我们自动完成，只要会写 Model 就行

Flask 使用对象关系映射 (Object Relational Mapping, ORM) 框架去操控数据库

ORM 对象关系映射，是一种程序技术，用于实现面向对象编程语言里不同类型系统的数据之间的转换

将对对象的操作转换为原生 SQL

> ORM 优点 \
> 1 易用性 可以有效减少重复 SQL \
> 2 性能损耗少 \
> 3 设计灵活，可以轻松实现复杂查询 \
> 4 移植性好


## Flask 的 ORM

Flask 使用 Python 自带的 ORM: SQLAlchemy

针对于 Flask 的支持 安装插件 flask-sqlalchemy

```bash
pip install flask-sqlalchemy
```

```python
'''
连接 SQLite
SQLite 连接的 URI
sqlite 一般是手机的数据库 一款轻量级数据库
这里不用密码 直接在本地即可
'''
DB_URI = sqlite:///sqlite3.db
```

```python
'''
连接 MySQL
'''
USERNAME = 'root'
PASSWORD = 'root'
HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'HelloFlask'

mysql+pymysql://USERNAME:PASSWORD@HOSTNAME:PORT/DATABASE

# 配置 URL
DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}
```

```python
'''
在 Flask 中使用 ORM
'''
# 连接数据库需要指定配置
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI  # 配置连接数据库路径 DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止对象追踪修改

# 在 Flask 项目中使用
db = SQLAlchemy()
db.init_app(app)
```

## Model 需要安装相关的包

```bash
用于 ORM
pip install flask-sqlalchemy -i https://pypi.douban.com/simple

用于数据迁移
pip install flask-migrate -i https://pypi.douban.com/simple

MySQL 驱动
pip install pymysql -i https://pypi.douban.com/simple
```
