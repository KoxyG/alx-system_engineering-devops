#!/usr/bin/python3
"""Exporting data in Json format"""


if __name__ == "__main__":
    import json
    import requests
    import sys

    userID = sys.argv[1]
    user = requests.get("https://jsonplacegolder.typicode.com/user/{}"
                        .format(userId))
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()

    todoUser = {}
    taskTodo = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('complete'),
                        "username": user.json().get('username')}
            taskTodo.append(taskDict)
    todoUser[userId] = taskTodo

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)

