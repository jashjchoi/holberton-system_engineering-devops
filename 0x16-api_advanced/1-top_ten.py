#!/usr/bin/python3
"""
queries the Reddit API and prints
the titles of the first 10 hot posts for a given subreddit
"""
import requests
from sys import argv


def top_ten(subreddit):
    """If not a valid subreddit, print None"""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    limit = {'limit': 10}
    headers = {'user-agent': 'request'}
    try:
        response = requests.get(url,
                                headers=headers,
                                limit=limit,
                                allow_redirects=False).json()
        data = response['data']['children']
        for post in data:
            title = post.get('data').get('title')
            print(title)
    except:
        print('None')
