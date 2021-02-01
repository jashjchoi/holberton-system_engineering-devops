#!/usr/bin/python3
"""
    Uses the fake API for a given employee ID
    returns information about todo list progress.
"""
from sys import argv
import requests

if __name__ == "__main__":
    id_emp = argv[1]
    url_employ = "https://jsonplaceholder.typicode.com/users/{}".format(id_emp)
    url_todos = url_employ + "/todos"
    req_employ = requests.get(url_employ).json()
    req_todos = requests.get(url_todos).json()
    name = req_employ.get("name")
    num_task = req_todos
    done_task = [task for task in req_todos if task.get("completed")]
    res = "Employee {} is done with tasks({}/{}):".format(
                name, len(done_task), len(num_task))
    for task in done_task:
        res += "\n\t " + task.get("title")
    print(res)
