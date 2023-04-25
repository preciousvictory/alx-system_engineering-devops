#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id_ = sys.argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        with urllib.request.urlopen('{}users?id={}'.format(url, id_)) as f:
            user = json.loads(f.read().decode())
            user_name = user[0].get("name")

        if user_name is not None:
            with urllib.request.urlopen('{}todos?userId={}'
                                        .format(url, id_)) as f:
                response = json.loads(f.read().decode())
                c = 0
                count_T = 0
                titles = []
                for i in response:
                    c += 1

                    if i.get("completed") is True:
                        count_T += 1
                        titles.append(i.get("title"))

            print(f'Employee {user_name} is done with tasks({count_T}/{c}):')
            for i in titles:
                print(f'\t {i}')
