#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """If an invalid subreddit is given, the function should return 0"""
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    try:
        response = requests.get(url,
                                headers={'user-agent': 'request'},
                                allow_redirects=False).json()
        return response['data'].get('subscribers')
    except:
        return 0
