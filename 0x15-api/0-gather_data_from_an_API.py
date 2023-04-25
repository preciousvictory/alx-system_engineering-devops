#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users?id={}".format(url, sys.argv[1])).json()
    todos = requests.get('{}todos?userId={}'.format(url, sys.argv[1])).json()

    completed = []
    for t in todos:
        if t.get("completed") is True:
            completed.append(t.get("title"))
    name = user[0].get("name")

    print("Employee {} is done with tasks({}/{}):".format(name,
          len(completed), len(todos)))
    for c in completed:
        print("\t {}".format(c))
