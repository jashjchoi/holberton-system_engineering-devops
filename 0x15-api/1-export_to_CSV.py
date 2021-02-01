#!/usr/bin/python3
"""
    Uses the fake API for a given employee ID
    export data in the CSV format
"""
import requests
from sys import argv
import csv

if __name__ == "__main__":
    """display the list of username and tasks in csv file"""
    id_emp = argv[1]
    FILE_NAME = id_emp + '.csv'
    url_emp = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(int(id_emp))
    EMPLOYEE_NAME = requests.get(url_emp).json()
    url_todos = ("https://jsonplaceholder.typicode.com/todos")
    req_todos = requests.get(url_todos).json()
    with open(FILE_NAME, mode='w', newline='') as csv_file:
        c_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)
        for todo in req_todos:
            if todo.get('userId') == int(id_emp):
                c_writer.writerow([todo.get("userId"),
                                    EMPLOYEE_NAME.get("username"),
                                    todo.get("completed"),
                                    todo.get("title")])
    