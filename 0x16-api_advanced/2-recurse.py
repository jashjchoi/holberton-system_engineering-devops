#!/usr/bin/python3
"""
    recursive function that queries the Reddit API
    and returns a list containing the titles of all hot articles
    If no results are found for the given subreddit
    the function should return None
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    headers = {'user-agent': 'user-agent'}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    try:
        req = requests.get(url, headers=headers, allow_redirects=False)
        if after is None:
            return hot_list
        else:
            for post in req.json().get('data').get('children'):
                hot_list.append(post.get('data').get('title'))
            new_after = req.json().get('data').get('after')
            recurse(subreddit, hot_list, after)
            return hot_list
    except:
        return None
