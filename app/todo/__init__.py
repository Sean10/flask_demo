#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26/03/2018 11:28 PM
# @Author  : Shark
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

todo_print = Blueprint('todo', __name__)

from . import view