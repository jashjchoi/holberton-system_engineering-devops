#!/usr/bin/python3
"""
    Uses the fake API for a given employee ID
    export data in the CSV format
"""
from requests import get
from sys import argv
import csv


if __name__ == '__main__':
    id_emp = argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + id_emp
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + id_emp
    names = get(url_user).json()
    todos = get(url_todos)
    FILE_NAME = "{}.csv".format(argv[1])

    with open(FILE_NAME, mode='w+', newline='') as csv_file:
        c_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)
        TASK_LIST = []
        for todo in todos.json():
            TASK_LIST.append(names.get("id"))
            TASK_LIST.append(names.get("username"))
            TASK_LIST.append(todo.get("completed"))
            TASK_LIST.append(todo.get("title"))
            c_writer.writerow(TASK_LIST)
            TASK_LIST = []
