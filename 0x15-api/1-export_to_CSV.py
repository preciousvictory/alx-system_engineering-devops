#!/usr/bin/python3
"""
a Python script that export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id_ = sys.argv[1]
    user = requests.get("{}users?id={}".format(url, id_)).json()
    todos = requests.get('{}todos?userId={}'.format(url, id_)).json()

    with open('{}.csv'.format(id_), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        data = [id_, user[0].get("username")]
        for t in todos:
            data = [id_, user[0].get("username")]
            data.append(t.get("completed"))
            data.append(t.get("title"))
            writer.writerow(data)
