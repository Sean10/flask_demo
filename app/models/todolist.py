#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 28/03/2018 12:33 AM
# @username  : Sean10
# @Site    : 
# @File    : todolist.py
# @Software: PyCharm

from bson.objectid import ObjectId
import html
import datetime

class TodoList:
    def __init__(self, default_config):
        self.collection = default_config['TODOS_COLLECTION']
        self.response = {'error': None, 'data': None}
        self.debug = default_config['DEBUG']

    def getTodoList(self, username):
        self.response['error'] = None
        cond = {}
        if username is not None:
            cond = {'username': username}

        try:
            # cursor = self.collection.find(cond).sort(
                # 'date', direction=-1).skip(skip).limit(limit)
            cursor = self.collection.find(cond).sort('date', direction=-1)

            self.response['data'] = []
            for todo in cursor:

                self.response['data'].append({'id': todo['_id'],
                                              'task': todo['task'],
                                              'date': todo['date'],
                                              'username': todo['username']})
        except Exception as e:
            self.print_debug_info(e, self.debug_mode)
            self.response['error'] = 'todos not found..'

        return self.response

    def get_todo_by_id(self, todo_id):
        self.response['error'] = None
        try:
            self.response['data'] = self.collection.find_one(
                {'_id': ObjectId(todo_id)})
        except Exception as e:
            self.print_debug_info(e, self.debug_mode)
            self.response['error'] = 'todo not found..'

        return self.response

    def get_total_count(self, username=None):
        cond = {}
        if username is not None:
            cond = {'username': username}

        return self.collection.find(cond).count()

    def create_new_todo(self, todo_data):
        self.response['error'] = None
        try:
            self.response['data'] = self.collection.insert(todo_data)
        except Exception as e:
            self.print_debug_info(e, self.debug_mode)
            self.response['error'] = 'Adding todo error..'

        return self.response

    def edit_todo(self, todo_id, todo_data):
        self.response['error'] = None
        del todo_data['date']

        try:
            self.collection.update(
                {'_id': ObjectId(todo_id)}, {"$set": todo_data}, upsert=False)
            self.response['data'] = True
        except Exception as e:
            self.print_debug_info(e, self.debug_mode)
            self.response['error'] = 'todo update error..'

        return self.response

    def delete_todo(self, todo_id):
        self.response['error'] = None
        try:
            if self.get_todo_by_id(todo_id) and self.collection.remove({'_id': ObjectId(todo_id)}):
                self.response['data'] = True
            else:
                self.response['data'] = False
        except Exception as e:
            self.print_debug_info(e, self.debug_mode)
            self.response['error'] = 'Deleting todo error..'

        return self.response

    @staticmethod
    def validate_todo_data(todo_data):
        # exp = re.compile('\W')
        # whitespace = re.compile('\s')
        # temp_title = whitespace.sub("_", todo_data['title'])
        # permalink = exp.sub('', temp_title)

        todo_data['task'] = html.escape(todo_data['task'])
        todo_data['date'] = datetime.datetime.utcnow()

        return todo_data

    @staticmethod
    def print_debug_info(msg, show=False):
        if show:
            import sys
            import os

            error_color = '\033[32m'
            error_end = '\033[0m'

            error = {'type': sys.exc_info()[0].__name__,
                     'file': os.path.basename(sys.exc_info()[2].tb_frame.f_code.co_filename),
                     'line': sys.exc_info()[2].tb_lineno,
                     'details': str(msg)}

            print(error_color)
            print('\n\n---\nError type: %s in file: %s on line: %s\nError details: %s\n---\n\n' \
                  % (error['type'], error['file'], error['line'], error['details']))
            print(error_end)