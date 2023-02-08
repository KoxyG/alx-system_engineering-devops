#!/usr/bin/python3
"""Returns information about an Employees ID"""

import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee))
    
    employeeName = employee.json().get('employeeName')

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    totalTasks = 0
    completed = []
    todos = response.json

    for task in todos:
        if task.get('completed'):
            completed.append(task)
            totalTasks += 1

    print("Employee {} is done with tasks ({}/{}):".format(employeeName, completed, totalTask))

    
    for task in todos:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
