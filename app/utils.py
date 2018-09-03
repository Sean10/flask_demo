#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 26/03/2018 9:54 PM
# @Author  : Shark
# @Site    : 
# @File    : utils.py
# @Software: PyCharm
import random
import string
import re
from flask import request, url_for, redirect, session, flash
from functools import wraps

def extract_tags(tags):
    '''

    :param tags: 通过逗号分割tag
    :return:
    '''
    whitespace = re.compile('\s')
    nowhite = whitespace.sub("", tags)
    tags_array = nowhite.split(',')

    cleaned = []
    for tag in tags_array:
        if tag not in cleaned and tag != "":
            cleaned.append(tag)

    return cleaned

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def login_required():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not session.get('user'):
                flash('You must be logged in..', 'error')
                return redirect(url_for('login'))
            return f(*args, **kwargs)

        return wrapped

    return wrapper

