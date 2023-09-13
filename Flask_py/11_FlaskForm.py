# -*- coding: utf-8 -*-
# @time    : 2023/9/13 9:26
# @author  : w-xin
# @file    : 11_FlaskForm.py
# @software: PyCharm

"""
flask form
flask 表单
"""
from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)

# RuntimeError: A secret key is required to use CSRF.
# 保护代码 数据  防止被入侵; 解决办法
app.config['SECRET_KEY'] = 'XINCON'


class Register(FlaskForm):
    """
    定义表单模型类
    """
    # label: 等于前端的标签; validators: 是列表形式 可以放多个验证
    user_name = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码', validators=[DataRequired('密码不能为空')])
    password2 = PasswordField(label='确认密码', validators=[DataRequired('密码不能为空'), EqualTo('password')])
    submit = SubmitField(label='提交')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    使用表单类
    :return:
    """
    form = Register()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            username = form.user_name.data
            password = form.user_name.data
            password2 = form.user_name.data
            print(username, password, password2)
        else:
            print('用户名或密码错误')
        return render_template('register.html', form=form)


if __name__ == '__main__':

    app.run()
