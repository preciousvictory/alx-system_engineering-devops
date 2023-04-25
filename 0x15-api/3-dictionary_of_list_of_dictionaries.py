#!/usr/bin/python3
"""a Python script that Records all tasks from all employees
and export data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(url)).json()

    data = {}
    for user in users:
        id_ = user.get('id')
        todos = requests.get('{}todos?userId={}'.format(url, id_)).json()

        info = []
        for t in todos:
            dict_ = {}
            dict_["task"] = t.get("title")
            dict_["completed"] = t.get("completed")
            dict_["username"] = user.get("username")
            info.append(dict_)

        data[id_] = info

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(data, outfile)
