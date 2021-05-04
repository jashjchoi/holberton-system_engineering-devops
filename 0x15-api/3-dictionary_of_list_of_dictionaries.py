#!/usr/bin/python3
"""
    Uses the fake API to export all data as JSON
"""
from requests import get
from sys import argv
import json

if __name__ == '__main__':
    req_user = get('https://jsonplaceholder.typicode.com/users').json()
    result = {}
    for usr in req_user:
        id_emp = usr["id"]
        req_todos = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(id_emp)).json()
        ALL_LIST = []
        for todo in req_todos:
            dict_task = {}
            dict_task["username"] = usr.get("username")
            dict_task["completed"] = todo.get("completed")
            dict_task["task"] = todo.get("title")
            ALL_LIST.append(dict_task)
        result[id_emp] = ALL_LIST
    with open("todo_all_employees.json", mode='w+', newline='') as json_file:
        json_file.write(json.dumps(result))
