#!/usr/bin/python3
"""Eporting data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/user/{}"
                        .format(userId))
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = userId + ".csv"
    with open(filename, mode='w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, name, task.get("completed"),
                                tasks.("title")])
