# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:02:18 2019

@author: yuntian.yang
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:41:26 2019

@author: yuntian.yang
"""
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import sqlite3

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id)) # See syntax

parser = reqparse.RequestParser()    # THIS ONE
parser.add_argument('task')      # THIS ONE

# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]faT
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()  # THIS ONE
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1  # THIS ONE
        todo_id = 'todo%i' % todo_id            # THIS ONE
        TODOS[todo_id] = {'task': args ['task']} 
        return TODOS[todo_id], 201

## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
# api.add_resource()

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/')
def homepage():
    return 'Welcome to the main page, the page of nothing!'

@app.route('/search')
def searchpage():
    key = input('Which knuckle head are you looking for?!') # key as in name, dob, primary_key in db
    # access data base and pull node/edge data via db.excute('SQL language')
    return 'Which knuckle head are you looking for?!'
    # return data and visualization

parser = reqparse.RequestParser()

if __name__ == '__main__':
    app.run(debug=True)