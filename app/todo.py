#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/08/2018 11:22 PM
# @Author  : sean10
# @Site    : 
# @File    : todo.py
# @Software: PyCharm

"""


"""


from flask import Blueprint, request, template_rendered, current_app, session, jsonify, render_template, \
    redirect, url_for, flash
from .utils import login_required
from .models.todolist import TodoList
from datetime import datetime

todo_print = Blueprint('todo', __name__)

# with
todoClass = None

def init_class_todo(app):
    global todoClass
    todoClass = TodoList(app.config)


@todo_print.route('/')
@login_required()
def index(todos=None):
    """
    获取完整Todolist
    :return:
    """

    user = session['user']
    print(user)
    if not todos:
        todos = todoClass.getTodoList(user['username'])
    print(todos['data'])
    return render_template('todolist.html',todos=todos['data'])


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

@todo_print.route('/new_todo', methods=['GET','POST'])
def new_todo():
    if request.method == 'GET':
        return render_template("new_todo.html")
    date = datetime.now()
    # .isoformat('T', timespec='milliseconds')
    postdata = {'task': request.form.get('task-full'),
                'username': session['user']['username'],
                'date': date}
    print(postdata)
    todos=todoClass.create_new_todo(postdata)
    flash("成功添加新todo")
    return redirect(url_for("todo.index"))

@todo_print.route('/delete_todo?id=<id>', methods=['GET'])
def delete_todo(id):
    ret = todoClass.delete_todo(id)
    if ret:
        flash("成功删除")
    else:
        flash("删除失败")
    return redirect(url_for("todo.index"))

@todo_print.route('/edit_todo?id=<id>', methods=['GET'])
def edit_todo(id):
    return "hello world"