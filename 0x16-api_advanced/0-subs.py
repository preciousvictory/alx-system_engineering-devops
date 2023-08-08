#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'preciousvicky_'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    res = response.json()
    if response.status_code == 200:
        return (res['data']['subscribers'])
    return (0)
