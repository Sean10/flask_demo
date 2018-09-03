#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26/03/2018 9:31 PM
# @Author  : Shark
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask, current_app, Blueprint
from .models import todolist
from .todo import todo_print, init_class_todo
from .blog import blog_print, init_class_blog
from .models import user, post, settings, todolist





def create_app(config=None):
    app = Flask(__name__, static_folder="../static", template_folder="../templates")

    app.config.from_object(config)
    app.config.from_envvar('APP_SETTINGS', silent=True)

    # bootstrap.init_app(app)
    # api.init_app(app)
    # with app.app_context():
    app.app_context().push()

    # db.init_app(app)
    # print(app.app_context().app)
    # print(app.blueprints)
    # configure_uploads(app, files)
    # patch_request_class(app)
    init_class_blog(app)
    init_class_todo(app)


    if isinstance(todo_print, Blueprint):
        app.register_blueprint(todo_print, url_prefix='/todo')

    if isinstance(blog_print, Blueprint):
        # print(blog)
        app.register_blueprint(blog_print, url_prefix='/blog')




    return app
#

    # def register_blueprints(app):
#     """Register all blueprint modules
#     Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
#     """
#     for name in find_modules('app'):
#         mod = import_string(name)
#         if hasattr(mod, 'main'):
#             app.register_blueprint(mod.bp)
#     return None