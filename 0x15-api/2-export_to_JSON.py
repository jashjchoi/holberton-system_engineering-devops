#!/usr/bin/python3
"""
    Uses the fake API for a given employee ID
    export data as JSON
"""
from requests import get
from sys import argv
import csv
import json

if __name__ == '__main__':
    id_emp = argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + id_emp
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + id_emp
    names = get(url_user).json()
    todos = get(url_todos).json()
    username = names.get("username")
    num_task = todos
    result = {}
    TASK_LIST = []
    for todo in num_task:
        dict_task = {}
        dict_task["username"] = str(username)
        dict_task["completed"] = todo.get("completed")
        dict_task["task"] = str(todo.get("title"))
        TASK_LIST.append(dict_task)
        result = {}
    result.update({names.get("id"): TASK_LIST})
    FILE_NAME = "{}.json".format(id_emp)
    with open(FILE_NAME, mode='w+', newline='') as json_file:
        json_file.write(json.dumps(result))
