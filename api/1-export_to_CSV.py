#!/usr/bin/python3
"""Records all tasks that are owned by this employee"""


import requests
from sys import argv

if __name__ == "__main__":
    """ employee info"""

    clients_id = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                              .format(argv[1]))
    all = clients_id.json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    user = user.json()
    with open(str(user.get('id'))+".csv", 'w') as f:
        for todo in all:
            f.write('"{}","{}","{}","{}"\n'
                    .format(user.get('id'), user.get('username'),
                            todo.get('completed'), todo.get('title')))
