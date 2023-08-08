#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returns a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit,
    the function should return None."""
    global after
    headers = {'User-Agent': 'preciousvicky_'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {
        "after": after,
        }

    res = requests.get(url, headers=headers, allow_redirects=False,
                       params=params)
    resp = res.json()

    if res.status_code == 200:
        after = resp.get('data').get('after')

        titles = resp.get('data').get('children')
        for title in titles:
            hot_list.append(title.get('data').get('title'))

        if after is not None:
            return recurse(subreddit, hot_list)

        return hot_list

    else:
        return (None)
