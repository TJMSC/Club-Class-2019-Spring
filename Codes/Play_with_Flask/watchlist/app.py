# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request, redirect,flash, url_for
app = Flask(__name__)

print("__name__ : ",__name__)

name = 'xxx'

message_board = [
    {'name': 'Tony', 'body': '我们'},
    {'name': 'Jenny', 'body':'一起'},
    {'name': 'Gogo', 'body':'学猫叫'},

    {'name': '张三', 'body': '一起'},
    {'name': '李四', 'body': '喵喵喵'},
    {'name': 'X五', 'body': '喵喵'},
]


@app.route('/')
def helloworld():
    return '<h1>Hello world</h1>'


@app.route('/msg-board', methods=['POST', 'GET'])
def index():
    # 如果是POST请求
    if request.method == 'POST':
        _name = request.form.get('name')
        _body = request.form.get('body')

        # TODO: 验证数据

        message_board.append({'name': _name, 'body' : _body})
    #     flash('Im added!')
        return redirect(url_for('index'))

    return render_template('index.html', name=name, message_board = message_board)
