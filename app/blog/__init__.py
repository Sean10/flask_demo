#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 07/08/2018 9:29 PM
# @Author  : sean10
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

blog_print = Blueprint('blog', __name__)

from . import view
