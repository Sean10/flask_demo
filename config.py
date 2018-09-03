import pymongo

class config():
    DEBUG = True
    CONNECTION_STRING = "mongodb://localhost:26789"  # replace it with your settings
    CONNECTION = pymongo.MongoClient(CONNECTION_STRING)

    '''Leave this as is if you don't have other configuration'''
    DATABASE = CONNECTION.blog
    POSTS_COLLECTION = DATABASE.posts
    USERS_COLLECTION = DATABASE.users
    SETTINGS_COLLECTION = DATABASE.settings
    DATABASE_TODO = CONNECTION.todo
    TODOS_COLLECTION = DATABASE_TODO.TodoList
    SECRET_KEY = 'development key'

# 数据库账户密码123

# 博客用户账号sean10密码123