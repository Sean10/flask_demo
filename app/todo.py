#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/08/2018 11:22 PM
# @Author  : sean10
# @Site    : 
# @File    : todo.py
# @Software: PyCharm

"""


"""


from flask import Blueprint, request, template_rendered, current_app, session
from .utils import login_required
from .models import todolist

todo_print = Blueprint('todo', __name__)

# with
# todoClass = todolist.TodoList(current_app.config)


# def getTodoList():
#     """
#     获取完整Todolist
#     :return:
#     """
#     re_uid = request.cookies.get('uid')
#     # TODOS = TodoList.query.filter_by(user=re_uid)
#     # print(type(TODOS))
#     # result = schema.dump(TODOS, many=True)
#     # print(result.data)
#     # return jsonify(result.data), 200

@todo_print.route('/')
def index():
    return "hello, world"

# @todo_print.route('/', default={'page': 1})
# @todo_print.route('/page-<int:page>', methods=['GET'])
# def index(page):
#     """
#
#     :return:
#     """
#     # skip = (page - 1) * int()
#     #todos = todoClass.todosgetTodoList(session['user']['username'])
#     #return template_rendered("todoList.html", todos=todos['data'], meta_title=current_app.config['BLOG_TITLE'])
#     return "hello,w rol"

@todo_print.route('/new_todo', methods=['POST'])
def new_todo():
    return ""
