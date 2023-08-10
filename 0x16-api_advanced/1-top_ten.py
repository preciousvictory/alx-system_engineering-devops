#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a
    given subreddit"""
    headers = {'User-Agent': 'preciousvicky_'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    res = response.json()
    if response.status_code == 200:
        c = 0
        for hot in res.get('data').get('children'):
            if c == 10:
                return
            print(hot.get('data').get('title'))
            c += 1
        return
    print('None')
