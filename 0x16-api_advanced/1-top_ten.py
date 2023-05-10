#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a
    given subreddit"""
    headers = {'User-Agent': 'preciousvicky_'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    resp = res.json()

    if res.status_code == 200:
        i = 0
        while (i < 10):
            print(resp.get('data').get('children')[i].get('data').get('title'))
            i += 1
    else:
        print(None)
