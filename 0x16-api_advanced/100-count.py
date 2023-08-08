#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
after = None
inx = 0


def word_filter(word_list):
    mydict = {}
    mynewList = []
    for elem in word_list:
        if elem.lower() in mydict:
            continue
        else:
            mydict[elem.lower()] = elem.lower()
            mynewList.append(elem.lower())
    return (mynewList)


def count_words(subreddit, word_list, i=inx, count={}):
    """a recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces."""
    global after

    recurse = __import__('2-recurse').recurse
    hot_list = recurse(subreddit)

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
        words = word_filter(word_list)

        if len(count) == 0:
            for word in words:
                count[word] = 0

        c = 0
        for hots in hot_list:
            if words[i] in hots.lower():
                c += 1
                count[words[i]] = c
        i += 1

        if i == len(words):
            for key, val in count.items():
                if val != 0:
                    print('{}: {}'.format(key, val))
            return

        if after is not None and i < len(word_list):
            count_words(subreddit, word_list, i, count)

    else:
        return (None)
