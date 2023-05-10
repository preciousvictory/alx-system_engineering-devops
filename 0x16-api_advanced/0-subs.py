#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Return the number of subcribers"""
    headers = {'User-Agent': 'preciousvicky_'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    resp = res.json()

    if res.status_code == 200:
        return (resp.get('data').get('subscribers'))
    return (0)
