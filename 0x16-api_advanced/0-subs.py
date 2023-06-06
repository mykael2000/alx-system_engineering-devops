#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    user = 'Mozilla/5.0'

    headers = {
        'User-Agent': user
    }

    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(link, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return res.json()['data']['subscribers']
