#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import urllib.request
import sys


id = sys.argv[1]

with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users?id={}'.format(id)) as f:
    user = json.loads(f.read().decode())
    user_name = user[0].get("name")

with urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)) as f:
    response = json.loads(f.read().decode())
    c = 0
    count_T = 0
    titles = []
    for i in response:
        c += 1
        if i.get("completed") == True:
            count_T += 1
            titles.append(i.get("title"))

print(f'Employee {user_name} is done with tasks({count_T}/{c}):')
for i in titles:
    print(f'     {i}')
