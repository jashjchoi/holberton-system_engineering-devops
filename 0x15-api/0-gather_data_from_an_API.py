#!/usr/bin/python3
"""
    Uses the fake API for a given employee ID
    returns information about todo list progress.
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    """display the title of completed tasks"""
    URL = 'https://jsonplaceholder.typicode.com'
    name = get(URL + '/users/' + argv[1]).json().get('name')
    tasks = get(URL + '/users/' + argv[1] + '/todos').json()
    done_tasks = []
    for task in tasks:
        if task.get('completed') is True:
            done_tasks.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        name, len(done_tasks), len(tasks)))
    if len(done_tasks) > 0:
        for task in done_tasks:
            print('\t {}'.format(task))
