#!/usr/bin/python3
"""Records all tasks that are owned by this employee specific"""


import json
import requests
from sys import argv

if __name__ == "__main__":
    clients_id = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                              .format(argv[1])).json()

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()

    peoples_dict = {str(user.get('id')): []}
    for todo in clients_id:
        td = {"task": todo.get('title'),
              "completed": todo.get('completed'),
              "username": user.get('username')}
        peoples_dict[str(user.get('id'))].append(td)

    with open(str(user.get('id'))+".json", 'w') as f:
        json.dump(peoples_dict, f)
