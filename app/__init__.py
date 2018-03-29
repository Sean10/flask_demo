#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26/03/2018 9:31 PM
# @Author  : Shark
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask, current_app
from .models import todolist
from .blueprints import todo

from werkzeug.utils import find_modules, import_string

def create_app(config=None):
    app = Flask(__name__, static_folder="../static", template_folder="../templates")

    app.config.from_object(config)
    app.config.from_envvar('APP_SETTINGS', silent=True)

    # bootstrap.init_app(app)
    # api.init_app(app)
    # with app.app_context():
    app.app_context().push()

    # db.init_app(app)

    # configure_uploads(app, files)
    # patch_request_class(app)

    app.register_blueprint(todo, url_prefix="/todo")

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