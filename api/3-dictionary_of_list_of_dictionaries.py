#!/usr/bin/python3
"""Get todos from user."""
import json
import requests

if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo_all_employees = {}

    for tasks in user:
        todos = requests.get("""
                https://jsonplaceholder.typicode.com/users/{}/todos
                """.format(str(tasks.get('id')))).json()
        todo_all_employees[str(tasks.get('id'))] = []
        for todo in todos:
            td = {"username": tasks.get('username'),
                  "task": todo.get('title'),
                  "completed": todo.get('completed')}
            todo_all_employees[str(tasks.get('id'))].append(td)

    with open("todo_all_employees.json", 'w') as f:
        json.dump(todo_all_employees, f)
