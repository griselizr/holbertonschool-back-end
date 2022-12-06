#!/usr/bin/python3
"""returns information about his/her 
TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    """ employee information """

    clients_id = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                              .format(argv[1]))
    all = clients_id.json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    user = user.json()
    list = []
    for todo in all:
        if todo.get('completed'):
            list.append(todo)
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(list), len(all)))
    for todo in list:
        print("\t {}".format(todo.get('title')))
