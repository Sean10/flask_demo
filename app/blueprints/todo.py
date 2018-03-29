
from flask import Blueprint, request, template_rendered, current_app, session
from ..utils import login_required
from ..models import todolist
todo = Blueprint('todo', __name__)

# with
todoClass = todolist.TodoList(current_app.config)


# @todo.route('/', methods=['GET'])
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

@todo.route('/', default={'page': 1})
@todo.route('/page-<int:page>', methods=['GET'])
@login_required()
def index(page):
    """

    :return:
    """
    # skip = (page - 1) * int()
    todos = todoClass.getTodoList(session['user']['username'])
    return template_rendered("todoList.html", todos=todos['data'], meta_title=current_app.config['BLOG_TITLE'])

@todo.route('/new_todo', methods=['POST'])
@login_required()
def new_todo():
    return ""
