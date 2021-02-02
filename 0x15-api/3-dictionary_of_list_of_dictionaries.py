#!/usr/bin/python3
"""
    Uses the fake API to export all data as JSON
"""
from requests import get
from sys import argv
import json

if __name__ == '__main__':
    url_user = 'https://jsonplaceholder.typicode.com/users'
    users = get(url_user).json()
    result = {}
    for usr in users:
        id_emp = usr.get("id")
        url_todos = url_user + "/{}/todos".format(id_emp)
        req_todos = get(url_todos).json()
        username = usr.get("username")
        ALL_LIST = []
        for todo in req_todos:
            dict_task = {}
            dict_task["username"] = str(username)
            dict_task["completed"] = todo.get("completed")
            dict_task["task"] = str(todo.get("title"))
            ALL_LIST.append(dict_task)
        result[id_emp] = ALL_LIST
    with open("todo_all_employees.json", mode='w+', newline='') as json_file:
        json_file.write(json.dumps(result))
