#!/usr/bin/python3
"""
    Uses the fake API for a given employee ID
    returns information about todo list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """display the title of completed tasks"""
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_LIST = []
    id_emp = argv[1]
    url_emp = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(int(id_emp))
    EMPLOYEE_NAME = requests.get(url_emp).json()
    print("Employee {} is done with tasks"
          .format(EMPLOYEE_NAME.get('name')), end="")
    url_todos = ("https://jsonplaceholder.typicode.com/todos")
    req_todos = requests.get(url_todos).json()
    for todo in req_todos:
        if todo.get('userId') == int(id_emp):
            TOTAL_NUMBER_OF_TASKS += 1
            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_LIST.append(todo.get("title"))
    print('({}/{}):'.format(NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for TASK_TITLE in TASK_LIST:
        print('\t {}'.format(TASK_TITLE))
