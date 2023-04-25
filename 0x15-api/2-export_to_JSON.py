#!/usr/bin/python3
"""a Python script that to export data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id_ = sys.argv[1]
    user = requests.get("{}users?id={}".format(url, id_)).json()
    todos = requests.get('{}todos?userId={}'.format(url, id_)).json()

    info = []
    dict_ = {}
    for t in todos:
        dict_["task"] = t.get("title")
        dict_["completed"] = t.get("completed")
        dict_["username"] = user[0].get("username")
        info.append(dict_)

    data = {id_: info}

    with open("{}.json".format(id_), "w") as outfile:
        json.dump(data, outfile)
